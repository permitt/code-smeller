	private static final class ExpandAllAction implements Runnable {
		private final ISynchronizePageConfiguration configuration;

		private ExpandAllAction(ISynchronizePageConfiguration configuration) {
			this.configuration = configuration;
		}

		@Override
		public void run() {
			Viewer viewer = configuration.getPage().getViewer();
			if (viewer == null || viewer.getControl().isDisposed()
					|| !(viewer instanceof AbstractTreeViewer)) {
				return;
			}
			UIUtils.expandAll(((AbstractTreeViewer) viewer));
		}
	}