		@Override
		public void handleEvent (Event event) {
			   Label label = (Label)event.widget;
			   Shell shell = label.getShell ();
			   switch (event.type) {
				   	case SWT.MouseDown:	/* Handle a user Click */
				   		/* Extract our Data */
				   		Event e = new Event ();
				   		e.item = (TableItem) label.getData ("_TableItem_");
				   		Table table = ((TableItem) e.item).getParent();

				   		/* Construct the new Selection[] to show */
				   		TableItem [] newSelection = null;
				   		if (isCTRLDown(event)) {
				   			/* We have 2 scenario's.
				   			 * 	1) We are selecting an already selected element - so remove it from the selected indices
				   			 *  2) We are selecting a non-selected element - so add it to the selected indices
				   			 */
				   			TableItem[] sel = table.getSelection();
				   			for (int i = 0; i < sel.length; ++i) {
				   				if (e.item.equals(sel[i])) {
				   					// We are de-selecting this element
				   					newSelection = new TableItem[sel.length - 1];
				   					System.arraycopy(sel, 0, newSelection, 0, i);
				   					System.arraycopy(sel, i+1, newSelection, i, sel.length - i - 1);
				   					break;
				   				}
		   					}

				   			/*
				   			 * If we haven't created the newSelection[] yet, than we are adding the newly selected element
				   			 * into the list of selected indicies
				   			 */
				   			if (newSelection == null) {
				   				newSelection = new TableItem[sel.length + 1];
				   				System.arraycopy(sel, 0, newSelection, 0, sel.length);
				   				newSelection[sel.length] = (TableItem) e.item;
				   			}

				   		} else {
				   			/* CTRL is not down, so we simply select the single element */
				   			newSelection = new TableItem[] { (TableItem) e.item };
				   		}
				   		/* Set the new selection of the table and notify the listeners */
				   		table.setSelection (newSelection);
				   		table.notifyListeners (SWT.Selection, e);

				   		/* Remove the Tooltip */
				   		shell.dispose ();
				   		table.setFocus();
				   		break;
				   	case SWT.MouseExit:
				   		shell.dispose ();
				   		break;
			   }
	    }};