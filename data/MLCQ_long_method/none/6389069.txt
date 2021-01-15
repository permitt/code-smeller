    private FocusListener getButtonFocusListener() {
    	if (buttonFocusListener == null) {
    		buttonFocusListener = new FocusListener() {

				@Override
				public void focusGained(FocusEvent e) {
					// Do nothing
				}

				@Override
				public void focusLost(FocusEvent e) {
					DialogCellEditor.this.focusLost();
				}
    		};
    	}

    	return buttonFocusListener;
	}