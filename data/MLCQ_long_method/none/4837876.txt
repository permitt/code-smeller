    @Override
    public void process(final ProcessClassContext processClassContext) {
        removeIgnoredMethods(processClassContext.getCls(), processClassContext);
    }