    public void open(final boolean remove) {
        if (remove) {
            rolePermissionsMap.clear();
            unchecked = null;
            excluded = null;
        }
        state = OPEN;
    }