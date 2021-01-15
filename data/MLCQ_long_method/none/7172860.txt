    public <TValue> void addIfNotEmpty(String parameterName, List<TValue> values) {
        if (values != null && !values.isEmpty()) {
            put(parameterName, StringUtil.join(",", values)); //$NON-NLS-1$
        }
    }