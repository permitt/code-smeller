	private void findObjectsToPack(@NonNull ProgressMonitor countingMonitor,
			@NonNull ObjectWalk walker, @NonNull Set<? extends ObjectId> want,
			@NonNull Set<? extends ObjectId> have,
			@NonNull Set<? extends ObjectId> noBitmaps) throws IOException {
		final long countingStart = System.currentTimeMillis();
		beginPhase(PackingPhase.COUNTING, countingMonitor, ProgressMonitor.UNKNOWN);

		stats.interestingObjects = Collections.unmodifiableSet(new HashSet<ObjectId>(want));
		stats.uninterestingObjects = Collections.unmodifiableSet(new HashSet<ObjectId>(have));
		excludeFromBitmapSelection = noBitmaps;

		canBuildBitmaps = config.isBuildBitmaps()
				&& !shallowPack
				&& have.isEmpty()
				&& (excludeInPacks == null || excludeInPacks.length == 0);
		if (!shallowPack && useBitmaps) {
			BitmapIndex bitmapIndex = reader.getBitmapIndex();
			if (bitmapIndex != null) {
				BitmapWalker bitmapWalker = new BitmapWalker(
						walker, bitmapIndex, countingMonitor);
				findObjectsToPackUsingBitmaps(bitmapWalker, want, have);
				endPhase(countingMonitor);
				stats.timeCounting = System.currentTimeMillis() - countingStart;
				stats.bitmapIndexMisses = bitmapWalker.getCountOfBitmapIndexMisses();
				return;
			}
		}

		List<ObjectId> all = new ArrayList<>(want.size() + have.size());
		all.addAll(want);
		all.addAll(have);

		final RevFlag include = walker.newFlag("include"); //$NON-NLS-1$
		final RevFlag added = walker.newFlag("added"); //$NON-NLS-1$

		walker.carry(include);

		int haveEst = have.size();
		if (have.isEmpty()) {
			walker.sort(RevSort.COMMIT_TIME_DESC);
		} else {
			walker.sort(RevSort.TOPO);
			if (thin)
				walker.sort(RevSort.BOUNDARY, true);
		}

		List<RevObject> wantObjs = new ArrayList<>(want.size());
		List<RevObject> haveObjs = new ArrayList<>(haveEst);
		List<RevTag> wantTags = new ArrayList<>(want.size());

		// Retrieve the RevWalk's versions of "want" and "have" objects to
		// maintain any state previously set in the RevWalk.
		AsyncRevObjectQueue q = walker.parseAny(all, true);
		try {
			for (;;) {
				try {
					RevObject o = q.next();
					if (o == null)
						break;
					if (have.contains(o))
						haveObjs.add(o);
					if (want.contains(o)) {
						o.add(include);
						wantObjs.add(o);
						if (o instanceof RevTag)
							wantTags.add((RevTag) o);
					}
				} catch (MissingObjectException e) {
					if (ignoreMissingUninteresting
							&& have.contains(e.getObjectId()))
						continue;
					throw e;
				}
			}
		} finally {
			q.release();
		}

		if (!wantTags.isEmpty()) {
			all = new ArrayList<>(wantTags.size());
			for (RevTag tag : wantTags)
				all.add(tag.getObject());
			q = walker.parseAny(all, true);
			try {
				while (q.next() != null) {
					// Just need to pop the queue item to parse the object.
				}
			} finally {
				q.release();
			}
		}

		if (walker instanceof DepthWalk.ObjectWalk) {
			DepthWalk.ObjectWalk depthWalk = (DepthWalk.ObjectWalk) walker;
			for (RevObject obj : wantObjs) {
				depthWalk.markRoot(obj);
			}
			// Mark the tree objects associated with "have" commits as
			// uninteresting to avoid writing redundant blobs. A normal RevWalk
			// lazily propagates the "uninteresting" state from a commit to its
			// tree during the walk, but DepthWalks can terminate early so
			// preemptively propagate that state here.
			for (RevObject obj : haveObjs) {
				if (obj instanceof RevCommit) {
					RevTree t = ((RevCommit) obj).getTree();
					depthWalk.markUninteresting(t);
				}
			}

			if (unshallowObjects != null) {
				for (ObjectId id : unshallowObjects) {
					depthWalk.markUnshallow(walker.parseAny(id));
				}
			}
		} else {
			for (RevObject obj : wantObjs)
				walker.markStart(obj);
		}
		for (RevObject obj : haveObjs)
			walker.markUninteresting(obj);

		final int maxBases = config.getDeltaSearchWindowSize();
		Set<RevTree> baseTrees = new HashSet<>();
		BlockList<RevCommit> commits = new BlockList<>();
		Set<ObjectId> roots = new HashSet<>();
		RevCommit c;
		while ((c = walker.next()) != null) {
			if (exclude(c))
				continue;
			if (c.has(RevFlag.UNINTERESTING)) {
				if (baseTrees.size() <= maxBases)
					baseTrees.add(c.getTree());
				continue;
			}

			commits.add(c);
			if (c.getParentCount() == 0) {
				roots.add(c.copy());
			}
			countingMonitor.update(1);
		}
		stats.rootCommits = Collections.unmodifiableSet(roots);

		if (shallowPack) {
			for (RevCommit cmit : commits) {
				addObject(cmit, 0);
			}
		} else {
			int commitCnt = 0;
			boolean putTagTargets = false;
			for (RevCommit cmit : commits) {
				if (!cmit.has(added)) {
					cmit.add(added);
					addObject(cmit, 0);
					commitCnt++;
				}

				for (int i = 0; i < cmit.getParentCount(); i++) {
					RevCommit p = cmit.getParent(i);
					if (!p.has(added) && !p.has(RevFlag.UNINTERESTING)
							&& !exclude(p)) {
						p.add(added);
						addObject(p, 0);
						commitCnt++;
					}
				}

				if (!putTagTargets && 4096 < commitCnt) {
					for (ObjectId id : tagTargets) {
						RevObject obj = walker.lookupOrNull(id);
						if (obj instanceof RevCommit
								&& obj.has(include)
								&& !obj.has(RevFlag.UNINTERESTING)
								&& !obj.has(added)) {
							obj.add(added);
							addObject(obj, 0);
						}
					}
					putTagTargets = true;
				}
			}
		}
		commits = null;

		if (thin && !baseTrees.isEmpty()) {
			BaseSearch bases = new BaseSearch(countingMonitor, baseTrees, //
					objectsMap, edgeObjects, reader);
			RevObject o;
			while ((o = walker.nextObject()) != null) {
				if (o.has(RevFlag.UNINTERESTING))
					continue;
				if (exclude(o))
					continue;

				int pathHash = walker.getPathHashCode();
				byte[] pathBuf = walker.getPathBuffer();
				int pathLen = walker.getPathLength();
				bases.addBase(o.getType(), pathBuf, pathLen, pathHash);
				filterAndAddObject(o, o.getType(), pathHash, want);
				countingMonitor.update(1);
			}
		} else {
			RevObject o;
			while ((o = walker.nextObject()) != null) {
				if (o.has(RevFlag.UNINTERESTING))
					continue;
				if (exclude(o))
					continue;
				filterAndAddObject(o, o.getType(), walker.getPathHashCode(), want);
				countingMonitor.update(1);
			}
		}

		for (CachedPack pack : cachedPacks)
			countingMonitor.update((int) pack.getObjectCount());
		endPhase(countingMonitor);
		stats.timeCounting = System.currentTimeMillis() - countingStart;
		stats.bitmapIndexMisses = -1;
	}