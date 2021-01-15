	private static void checkComputedListDiff(List<Object> oldList, List<Object> newList) {
		ListDiff diff = Diffs.computeListDiff(oldList, newList);

		final List<Object> list = new ArrayList<Object>(oldList);
		diff.accept(new ListDiffVisitor() {
			@Override
			public void handleAdd(int index, Object element) {
				list.add(index, element);
			}

			@Override
			public void handleRemove(int index, Object element) {
				assertEquals(element, list.remove(index));
			}

			@Override
			public void handleReplace(int index, Object oldElement, Object newElement) {
				assertEquals(oldElement, list.set(index, newElement));
			}
		});

		assertEquals("Applying diff to old list should make it equal to new list", newList, list);
	}