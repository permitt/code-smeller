    public ProjectCloseListener(final ProjectRepositoryManager projectManager) {
        Check.notNull(projectManager, "projectManager"); //$NON-NLS-1$

        this.projectManager = projectManager;
    }