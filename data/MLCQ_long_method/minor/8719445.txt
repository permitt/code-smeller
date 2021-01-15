	public static void main(String[] args) {
		Display display = new Display();
		Shell shell = new Shell(display);
		shell.setText("Excel Sheet Selection Example");
		shell.setLayout(new FillLayout());
		OleAutomation application;
		try {
			OleFrame frame = new OleFrame(shell, SWT.NONE);
			OleControlSite controlSite = new OleControlSite(frame, SWT.NONE, "Excel.Sheet");
			controlSite.doVerb(OLE.OLEIVERB_INPLACEACTIVATE);
			
			OleAutomation excelSheet = new OleAutomation(controlSite);
			int[] dispIDs = excelSheet.getIDsOfNames(new String[] { "Application" });
			Variant pVarResult = excelSheet.getProperty(dispIDs[0]);
			application = pVarResult.getAutomation();
			pVarResult.dispose();
			excelSheet.dispose();
			
			OleListener listener = new OleListener() {
				@Override
				public void handleEvent(OleEvent e) {
					// SheetSelectionChange(ByVal Sh As Object, ByVal Target As Excel.Range)
					Variant[] args = e.arguments;
					// OleAutomation sheet = args[1].getAutomation(); // Excel.Sheet
					OleAutomation range = args[0].getAutomation(); // Excel.Range
					int[] dispIDs = range.getIDsOfNames(new String[] { "Row" });
					Variant pVarResult = range.getProperty(dispIDs[0]);
					int row = pVarResult.getInt();
					dispIDs = range.getIDsOfNames(new String[] { "Column" });
					pVarResult = range.getProperty(dispIDs[0]);
					int column = pVarResult.getInt();
					range.dispose();
					System.out.println("row=" + row + " column=" + column);
				}
			};
			controlSite.addEventListener(application, IID_AppEvents, SheetSelectionChange, listener);
		} catch (SWTError e) {
			System.out.println("Unable to open activeX control");
			display.dispose();
			return;
		}
		shell.setSize(800, 600);
		shell.open();
		while (!shell.isDisposed()) {
			if (!display.readAndDispatch())
				display.sleep();
		}
		if (application != null) application.dispose();
		display.dispose();
	}