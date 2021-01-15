public void remove (int [] indices) {
	checkWidget ();
	if (indices == null) error (SWT.ERROR_NULL_ARGUMENT);
	if (indices.length == 0) return;
	int [] newIndices = new int [indices.length];
	System.arraycopy (indices, 0, newIndices, 0, indices.length);
	sort (newIndices);
	int start = newIndices [newIndices.length - 1], end = newIndices [0];
	if (!(0 <= start && start <= end && end < itemCount)) {
		error (SWT.ERROR_INVALID_RANGE);
	}
	int last = -1;
	for (int i=0; i<newIndices.length; i++) {
		int index = newIndices [i];
		if (index != last) {
			TableItem item = items [index];
			if (item != null) item.release (false);
			if (index != itemCount - 1) fixSelection (index, false);
			System.arraycopy (items, index + 1, items, index, --itemCount - index);
			items [itemCount] = null;
			last = index;
		}
	}
	updateRowCount();
	if (itemCount == 0) {
		setTableEmpty ();
	}
}