    public STExpandAllTreeAction(AbstractSTTreeViewer stViewer) {
        super(STDataViewersMessages.expandAllAction_title,
                AbstractUIPlugin.imageDescriptorFromPlugin(STDataViewersActivator.PLUGIN_ID,
                        "icons/expand_all.gif")); //$NON-NLS-1$
        this.stViewer = stViewer;
    }