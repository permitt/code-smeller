	@Override
	public StyleRange[] getStyleRanges(int offset, int length) {
		List<StyleRange> result = new ArrayList<>();
		// get the sublist with length = 0 so that it will return all with that
		// offset.
		StyleRange sr = new StyleRange(offset, 0, null, null, SWT.NO);
		for (Iterator<StyleRange> iterator = ranges.tailSet(sr).iterator(); iterator.hasNext();) {
			StyleRange r = iterator.next();
			if (r.start >= offset && r.start + r.length <= offset + length)
				result.add((StyleRange) r.clone());
			else
				break;
		}

		if (result.size() > 0)
			return result.toArray(new StyleRange[result.size()]);

		sr.length = length;
		return new StyleRange[] { sr };
	}