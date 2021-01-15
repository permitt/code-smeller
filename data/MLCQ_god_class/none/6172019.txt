	private final static class SpellcheckableMessageAreaExtension
			extends SpellcheckableMessageArea {
		private SpellcheckableMessageAreaExtension(Composite parent,
				String initialText, boolean readOnly, int styles) {
			super(parent, initialText, readOnly, styles);
		}

		@Override
		protected void createMarginPainter() {
			// Disabled intentionally
		}
	}