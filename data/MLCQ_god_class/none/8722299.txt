public class Bug531667_Group_drawing_with_paint_listener_is_wrong {

	public static void main(String[] args) {
		final Display display = new Display();
		Shell shell = new Shell(display);
		shell.setLayout(new FillLayout());
		shell.setSize(200, 200);
		shell.setText("Bug 531667 paint inside a Group is wrong");

		final Group group = new Group(shell, SWT.NONE);
		group.setText("some group");
		group.setLayout(new FillLayout());

		final Image image = new Image(display, 40, 40);
		GC gc = new GC(image);
		gc.setBackground(display.getSystemColor(SWT.COLOR_DARK_RED));
		gc.fillRectangle(0,  0, 40, 40);
		gc.dispose();

		class DrawSquare implements PaintListener {
			@Override
			public void paintControl(PaintEvent e) {
			    GC gc = e.gc;
			    gc.drawImage(image, 0, 0);
			}
		}
		group.addPaintListener(new DrawSquare());

		shell.open();

		while (!shell.isDisposed()) {
			if (!display.readAndDispatch()) {
				display.sleep();
			}
		}
		display.dispose();
	}
}