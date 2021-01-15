    protected void assertNotClosed() throws SQLConnectionClosedException {
        this.statement.assertNotClosed();

        if (this.isClosed) {
            throw new SQLConnectionClosedException(format(Level.WARNING, "excp.closed_resultset", this.sql, getFile().getName()), this.sql, getFile());
        }
    }