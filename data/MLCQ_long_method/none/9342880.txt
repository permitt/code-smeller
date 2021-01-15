    @Override
    public boolean requestWindowFocus() {
        CEmbeddedFrame.updateGlobalFocusedWindow(target);
        target.synthesizeWindowActivation(true);
        return true;
    }