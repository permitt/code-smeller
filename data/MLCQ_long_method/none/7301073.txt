    public NonFatalErrorHelper(final Workspace workspace) {
        Check.notNull(workspace, "workspace"); //$NON-NLS-1$

        this.workspace = workspace;

        workspace.getClient().getEventEngine().addNonFatalErrorListener(listener);
    }