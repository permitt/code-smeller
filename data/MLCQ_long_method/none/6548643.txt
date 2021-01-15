    public void dispose() {
        if (workbenchWindow == null) {
            // action has already been disposed
            return;
        }
        workbenchWindow.removePageListener(this);
        workbenchWindow.getPartService().removePartListener(this);
        workbenchWindow = null;
    }