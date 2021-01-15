	protected void initialize() {
		GridLayout layout = new GridLayout(3, false);
		layout.marginWidth = 0;
		setLayout(layout);
		if (getParent().getLayout() instanceof GridLayout) {
			layout = (GridLayout) getParent().getLayout();
			setLayoutData(new GridData(SWT.FILL, SWT.TOP, true, false, layout.numColumns, 1));
		}
		toolkit.adapt(this);
		toolkit.paintBordersFor(this);
	}