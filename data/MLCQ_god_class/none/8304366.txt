	protected class EListIterator<E1> extends EIterator<E1> implements ListIterator<E1> {
		/**
		 * Creates an instance.
		 */
		public EListIterator() {
			super();
		}

		/**
		 * Creates an instance advanced to the index.
		 * 
		 * @param index
		 *            the starting index.
		 */
		public EListIterator(int index) {
			cursor = index;
		}

		/**
		 * Returns whether there are more objects for {@link #previous}. Returns whether there are more
		 * objects.
		 */
		public boolean hasPrevious() {
			return cursor != 0;
		}

		/**
		 * Returns the previous object and advances the iterator. This implementation delegates to
		 * {@link #doPrevious doPrevious}.
		 * 
		 * @return the previous object.
		 * @exception NoSuchElementException
		 *                if the iterator is done.
		 */
		@SuppressWarnings("unchecked")
		public E1 previous() {
			return (E1)doPrevious();
		}

		/**
		 * Returns the previous object and advances the iterator. This implementation delegates to
		 * {@link AbstractEList#get get}.
		 * 
		 * @return the previous object.
		 * @exception NoSuchElementException
		 *                if the iterator is done.
		 */
		protected E doPrevious() {
			try {
				E previous = get(--cursor);
				checkModCount();
				lastCursor = cursor;
				return previous;
			} catch (IndexOutOfBoundsException exception) {
				checkModCount();
				throw new NoSuchElementException();
			}
		}

		/**
		 * Returns the index of the object that would be returned by calling {@link #next() next}.
		 * 
		 * @return the index of the object that would be returned by calling <code>next</code>.
		 */
		public int nextIndex() {
			return cursor;
		}

		/**
		 * Returns the index of the object that would be returned by calling {@link #previous previous}.
		 * 
		 * @return the index of the object that would be returned by calling <code>previous</code>.
		 */
		public int previousIndex() {
			return cursor - 1;
		}

		/**
		 * Sets the object at the index of the last call to {@link #next() next} or {@link #previous previous}
		 * . This implementation delegates to {@link AbstractEList#set set}.
		 * 
		 * @param object
		 *            the object to set.
		 * @exception IllegalStateException
		 *                if <code>next</code> or <code>previous</code> have not yet been called, or
		 *                {@link #remove(Object) remove} or {@link #add add} have already been called after
		 *                the last call to <code>next</code> or <code>previous</code>.
		 */
		@SuppressWarnings("unchecked")
		public void set(E1 object) {
			doSet((E)object);
		}

		/**
		 * Sets the object at the index of the last call to {@link #next() next} or {@link #previous previous}
		 * . This implementation delegates to {@link AbstractEList#set set}.
		 * 
		 * @param object
		 *            the object to set.
		 * @exception IllegalStateException
		 *                if <code>next</code> or <code>previous</code> have not yet been called, or
		 *                {@link #remove(Object) remove} or {@link #add add} have already been called after
		 *                the last call to <code>next</code> or <code>previous</code>.
		 */
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

		/**
		 * Adds the object at the {@link #next() next} index and advances the iterator past it. This
		 * implementation delegates to {@link #doAdd(Object) doAdd(E)}.
		 * 
		 * @param object
		 *            the object to add.
		 */
		@SuppressWarnings("unchecked")
		public void add(E1 object) {
			doAdd((E)object);
		}

		/**
		 * Adds the object at the {@link #next() next} index and advances the iterator past it. This
		 * implementation delegates to {@link AbstractEList#add(int, Object) add(int, E)}.
		 * 
		 * @param object
		 *            the object to add.
		 */
		protected void doAdd(E object) {
			checkModCount();

			try {
				AbstractEList.this.add(cursor++, object);
				expectedModCount = modCount;
				lastCursor = -1;
			} catch (IndexOutOfBoundsException exception) {
				throw new ConcurrentModificationException();
			}
		}
	}