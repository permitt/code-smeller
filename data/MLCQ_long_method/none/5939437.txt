    public Object setProperty(final String key, final String value, final boolean isExternalProperty) {
        if (isExternalProperty) {
            System.setProperty(key, value);
        }
        return internalProperties.setProperty(key, value);
    }