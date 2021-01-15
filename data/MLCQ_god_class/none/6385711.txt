public class ObservableSetTreeContentProvider implements ITreeContentProvider {
	private final ObservableCollectionTreeContentProvider impl;

	private static class Impl extends ObservableCollectionTreeContentProvider {
		Impl(IObservableFactory setFactory,
				TreeStructureAdvisor structureAdvisor) {
			super(setFactory, structureAdvisor);
		}

		private class SetChangeListener implements ISetChangeListener {
			final Object parentElement;

			public SetChangeListener(Object parentElement) {
				this.parentElement = parentElement;
			}

			@Override
			public void handleSetChange(SetChangeEvent event) {
				if (isViewerDisposed())
					return;

				Set localAdditions = event.diff.getAdditions();
				Set localRemovals = event.diff.getRemovals();

				Set knownElementAdditions = ViewerElementSet
						.withComparer(comparer);
				knownElementAdditions.addAll(localAdditions);
				knownElementAdditions.removeAll(knownElements);

				Set knownElementRemovals = findPendingRemovals(parentElement,
						localRemovals);
				knownElementRemovals.retainAll(knownElements);

				knownElements.addAll(knownElementAdditions);
				if (realizedElements != null) {
					realizedElements.removeAll(knownElementRemovals);
				}

				for (Iterator iterator = localAdditions.iterator(); iterator
						.hasNext();) {
					Object child = iterator.next();
					getOrCreateNode(child).addParent(parentElement);
				}

				viewerUpdater.add(parentElement, localAdditions.toArray());
				viewerUpdater.remove(parentElement, localRemovals.toArray());

				for (Iterator iterator = localRemovals.iterator(); iterator
						.hasNext();) {
					Object child = iterator.next();
					TreeNode childNode = getExistingNode(child);
					if (childNode != null)
						childNode.removeParent(parentElement);
				}

				if (realizedElements != null) {
					realizedElements.addAll(knownElementAdditions);
				}
				knownElements.removeAll(knownElementRemovals);
			}
		}

		@Override
		protected IObservablesListener createCollectionChangeListener(
				Object parentElement) {
			return new SetChangeListener(parentElement);
		}

		@Override
		protected void addCollectionChangeListener(
				IObservableCollection collection, IObservablesListener listener) {
			IObservableSet set = (IObservableSet) collection;
			ISetChangeListener setListener = (ISetChangeListener) listener;
			set.addSetChangeListener(setListener);
		}

		@Override
		protected void removeCollectionChangeListener(
				IObservableCollection collection, IObservablesListener listener) {
			IObservableSet set = (IObservableSet) collection;
			ISetChangeListener setListener = (ISetChangeListener) listener;
			set.removeSetChangeListener(setListener);
		}
	}

	/**
	 * Constructs an ObservableListTreeContentProvider using the given list
	 * factory. Must be called from the display thread.
	 *
	 * @param setFactory
	 *            observable factory that produces an IObservableSet of children
	 *            for a given parent element. Observable sets created by this
	 *            factory must be on the realm of the current display.
	 * @param structureAdvisor
	 *            an advisor that will be consulted from the implementations of
	 *            the {@link #getParent(Object)} and
	 *            {@link #hasChildren(Object)} methods, or <code>null</code> if
	 *            no advisor is available. It is recommended that clients pass a
	 *            non-null advisor if they can provide additional structural
	 *            information about the tree.
	 */
	public ObservableSetTreeContentProvider(IObservableFactory setFactory,
			TreeStructureAdvisor structureAdvisor) {
		impl = new Impl(setFactory, structureAdvisor);
	}

	@Override
	public void inputChanged(Viewer viewer, Object oldInput, Object newInput) {
		impl.inputChanged(viewer, oldInput, newInput);
	}

	@Override
	public Object[] getElements(Object inputElement) {
		return impl.getElements(inputElement);
	}

	@Override
	public boolean hasChildren(Object element) {
		return impl.hasChildren(element);
	}

	@Override
	public Object[] getChildren(Object parentElement) {
		return impl.getChildren(parentElement);
	}

	@Override
	public Object getParent(Object element) {
		return impl.getParent(element);
	}

	/**
	 * Disposes of this content provider. This is called by the viewer when a
	 * content provider is replaced, or when the viewer itself is disposed.
	 * <p>
	 * The viewer should not be updated during this call, as it is in the
	 * process of being disposed.
	 * </p>
	 * <p>
	 * <em>Note:</em> Data binding content providers become unusable on
	 * disposal.
	 * </p>
	 */
	@Override
	public void dispose() {
		impl.dispose();
	}

	/**
	 * Returns the set of elements known to this content provider. Label
	 * providers may track this set if they need to be notified about additions
	 * before the viewer sees the added element, and notified about removals
	 * after the element was removed from the viewer. This is intended for use
	 * by label providers, as it will always return the items that need labels.
	 *
	 * @return readableSet of items that will need labels
	 */
	public IObservableSet getKnownElements() {
		return impl.getKnownElements();
	}

	/**
	 * Returns the set of known elements which have been realized in the viewer.
	 * Clients may track this set in order to perform custom actions on elements
	 * while they are known to be present in the viewer.
	 *
	 * @return the set of known elements which have been realized in the viewer.
	 * @since 1.3
	 */
	public IObservableSet getRealizedElements() {
		return impl.getRealizedElements();
	}
}