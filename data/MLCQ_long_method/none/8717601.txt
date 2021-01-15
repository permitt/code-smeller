	public static void main(String[] args) {
		Display display = new Display();
		Shell shell = new Shell(display);
		shell.setSize(400, 400);
		shell.setText("Bug 531667 GC transform is wrong");
		shell.setLayout(new FillLayout());
		Composite main = new Composite(shell, SWT.NONE);
		main.setLayout(new FillLayout());

		Composite[] squares = showCaseTransform(main);
		for (Composite square : squares) {
			square.layout();
		}

		shell.open();
		while (!shell.isDisposed()) {
			if (!display.readAndDispatch())
				display.sleep();
		}
		display.dispose();
	}