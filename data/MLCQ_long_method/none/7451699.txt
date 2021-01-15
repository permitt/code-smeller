    @Override
    public boolean isInConfiguration(IsInConfigurationAccess access) {
        return access.findClassByName("org.codehaus.groovy.reflection.ClassInfo") != null;
    }