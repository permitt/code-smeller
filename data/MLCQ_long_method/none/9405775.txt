    protected Container getGlobalCurrentFocusCycleRoot()
        throws SecurityException
    {
        synchronized (KeyboardFocusManager.class) {
            checkKFMSecurity();
            return currentFocusCycleRoot;
        }
    }