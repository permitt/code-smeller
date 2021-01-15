    protected void inputChanged(Object newInput, Object newSelection) {
        fFilterText.setText(""); //$NON-NLS-1$
        fTableViewer.setInput(newInput);
		selectFirstMatch();

        // Resize the table's height accordingly to the new input
        Table viewerTable = fTableViewer.getTable();
        Point tableSize = viewerTable.computeSize(SWT.DEFAULT, SWT.DEFAULT);
        int tableMaxHeight = fComposite.getDisplay().getBounds().height / 2;
        // removes padding if necessary
        int tableHeight = (tableSize.y <= tableMaxHeight) ? tableSize.y
                - viewerTable.getItemHeight() - viewerTable.getItemHeight() / 2
                : tableMaxHeight;
        ((GridData) viewerTable.getLayoutData()).heightHint = tableHeight;
        Point fCompSize = fComposite.computeSize(SWT.DEFAULT, SWT.DEFAULT);
        fComposite.setSize(fCompSize);
        fComposite.getShell().setSize(fCompSize);
    }