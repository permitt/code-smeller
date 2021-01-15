    public synchronized void reload() throws ItemNotFoundException, RepositoryException {
        if (isComplete()) {
            // nothing to do
            return;
        }

        NodeId id = parent.getWorkspaceId();
        Iterator<ChildInfo> childNodeInfos = factory.getItemStateFactory().getChildNodeInfos(id);
        update(childNodeInfos);
    }