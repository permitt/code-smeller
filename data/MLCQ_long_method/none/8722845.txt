	public void removeAccessibleEditableTextListener(AccessibleEditableTextListener listener) {
	    checkWidget();
	    if (listener == null) SWT.error(SWT.ERROR_NULL_ARGUMENT);
	    if (accessibleEditableTextListeners != null) {
	    	accessibleEditableTextListeners.remove(listener);
	    	if (accessibleEditableTextListeners.isEmpty()) accessibleEditableTextListeners = null;
	    }
	}