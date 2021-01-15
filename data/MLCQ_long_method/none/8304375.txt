		protected void doSet(E object) {
			if (lastCursor == -1) {
				throw new IllegalStateException();
			}
			checkModCount();

			try {
				AbstractEList.this.set(lastCursor, object);
			} catch (IndexOutOfBoundsException exception) {
				throw new ConcurrentModificationException();
			}
		}