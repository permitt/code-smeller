    private void fillLocalToolBar(IToolBarManager toolBarManager) {
        toolBarManager.add(refreshAction);
        toolBarManager.add(focusDialogActionToolbar);
        toolBarManager.add(new Separator());
        toolBarManager.add(historyAction);
        toolBarManager.add(forwardAction);
    }