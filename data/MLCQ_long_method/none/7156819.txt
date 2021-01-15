    @Override
    public boolean supportsSubqueriesInQuantifieds() throws SQLServerException {
        checkClosed();
        return true;
    }