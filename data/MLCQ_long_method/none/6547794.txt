    private WorkbenchWindow newWorkbenchWindow() {
        WorkbenchWindow wbw = ((WorkbenchImplementation) Tweaklets
                .get(WorkbenchImplementation.KEY)).createWorkbenchWindow(getNewWindowNumber());
        return wbw;
    }