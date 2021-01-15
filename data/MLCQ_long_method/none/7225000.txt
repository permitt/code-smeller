		@Override
		@Nullable
		public Object scanUnsafe(Attr key) {
			if (key == Attr.PARENT) return s;

			return InnerOperator.super.scanUnsafe(key);
		}