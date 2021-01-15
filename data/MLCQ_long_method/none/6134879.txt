		@Override
		public void customButtonPressed(ListDialogField field, int index) {
			switch (index) {
			case 0: /* add */
				editEntries(null);
				break;
			case 1: /* edit */
				List selected = field.getSelectedElements();
				editEntries((BPVariableElement) selected.get(0));
				break;
			}
		}