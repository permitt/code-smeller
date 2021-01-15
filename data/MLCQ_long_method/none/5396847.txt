    public String getQueryString() {
        return delegate.getClass().getName() + " doesn't support getQueryString() method: '" + delegate.toString() + "'";
    }