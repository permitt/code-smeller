    @Override
    Path buildPath(boolean workspacePath) throws RepositoryException {
        Path parentPath = parent.buildPath(workspacePath);
        return getPathFactory().create(parentPath, getName(), true);
    }