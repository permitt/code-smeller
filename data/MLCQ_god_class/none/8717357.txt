public class Snippet113 {

public static void main (String [] args) {
	Display display = new Display ();
	Shell shell = new Shell (display);
	Table table = new Table (shell, SWT.CHECK | SWT.BORDER | SWT.V_SCROLL | SWT.H_SCROLL);
	for (int i=0; i<12; i++) {
		TableItem item = new TableItem (table, SWT.NONE);
		item.setText ("Item " + i);
	}
	Rectangle clientArea = shell.getClientArea ();
	table.setBounds (clientArea.x, clientArea.y, 100, 100);
	table.addListener (SWT.Selection, event -> {
		String string = event.detail == SWT.CHECK ? "Checked" : "Selected";
		System.out.println (event.item + " " + string);
	});
	shell.setSize (200, 200);
	shell.open ();
	while (!shell.isDisposed()) {
		if (!display.readAndDispatch ()) display.sleep ();
	}
	display.dispose ();
}
}