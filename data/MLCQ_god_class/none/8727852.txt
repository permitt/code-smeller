public class Snippet144 {

static final int COUNT = 1000000;

public static void main(String[] args) {
	Display display = new Display ();
	final Shell shell = new Shell (display);
	shell.setLayout (new RowLayout (SWT.VERTICAL));
	final Table table = new Table (shell, SWT.VIRTUAL | SWT.BORDER);
	table.addListener (SWT.SetData, event -> {
		TableItem item = (TableItem) event.item;
		int index = table.indexOf (item);
		item.setText ("Item " + index);
		System.out.println (item.getText ());
	});
	table.setLayoutData (new RowData (200, 200));
	Button button = new Button (shell, SWT.PUSH);
	button.setText ("Add Items");
	final Label label = new Label(shell, SWT.NONE);
	button.addListener (SWT.Selection, event -> {
		long t1 = System.currentTimeMillis ();
		table.setItemCount (COUNT);
		long t2 = System.currentTimeMillis ();
		label.setText ("Items: " + COUNT + ", Time: " + (t2 - t1) + " (ms)");
		shell.layout ();
	});
	shell.pack ();
	shell.open ();
	while (!shell.isDisposed ()) {
		if (!display.readAndDispatch ()) display.sleep ();
	}
	display.dispose ();
}
}