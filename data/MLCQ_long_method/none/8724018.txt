public void setColumnOrder (int [] order) {
	checkWidget ();
	if (order == null) SWT.error (SWT.ERROR_NULL_ARGUMENT);
	if (columns.length == 0) {
		if (order.length != 0) SWT.error (SWT.ERROR_INVALID_ARGUMENT);
		return;
	}
	if (order.length != columns.length) SWT.error (SWT.ERROR_INVALID_ARGUMENT);
	boolean reorder = false;
	boolean [] seen = new boolean [columns.length];
	int[] oldOrder = getColumnOrder ();
	for (int i = 0; i < order.length; i++) {
		int index = order [i];
		if (index < 0 || index >= columns.length) SWT.error (SWT.ERROR_INVALID_RANGE);
		if (seen [index]) SWT.error (SWT.ERROR_INVALID_ARGUMENT);
		seen [index] = true;
		if (index != oldOrder [i]) reorder = true;
	}
	if (!reorder) return;

	headerHideToolTip ();
	int[] oldX = new int [columns.length];
	for (int i = 0; i < columns.length; i++) {
		oldX [i] = columns [i].getX ();
	}
	orderedColumns = new CTableColumn [order.length];
	for (int i = 0; i < order.length; i++) {
		orderedColumns [i] = columns [order [i]];
	}
	for (CTableColumn orderedColumn : orderedColumns) {
		CTableColumn column = orderedColumn;
		if (!column.isDisposed () && column.getX () != oldX [column.getIndex ()]) {
			column.notifyListeners (SWT.Move, new Event ());
		}
	}

	redraw ();
	if (drawCount <= 0 && header.isVisible ()) header.redraw ();
}