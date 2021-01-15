    protected void checkDuringManage() {
        if (!inManage.get() || app == null) {
            throw new IllegalStateException("Operation only permitted during manage, e.g. called from doBuild() of "+this);
        }
    }