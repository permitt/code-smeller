	private class TraversalFilterManager implements FocusListener {
		/** The managed filter. We only need one instance. */
		private TraversalFilter filter = new TraversalFilter();

		private boolean filtering = false;

		/**
		 * Attaches the global traversal filter.
		 *
		 * @param event
		 *            Ignored.
		 */
		@Override
		public void focusGained(FocusEvent event) {
			Display.getCurrent().addFilter(SWT.Traverse, filter);
			filtering = true;
		}

		/**
		 * Detaches the global traversal filter.
		 *
		 * @param event
		 *            Ignored.
		 */
		@Override
		public void focusLost(FocusEvent event) {
			Display.getCurrent().removeFilter(SWT.Traverse, filter);
			filtering = false;
		}

		/**
		 * Remove the traverse filter if we close without focusOut.
		 */
		public void dispose() {
			if (filtering) {
				Display.getCurrent().removeFilter(SWT.Traverse, filter);
			}
		}
	}