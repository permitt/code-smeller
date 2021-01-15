    public void finer(String msg) {
        if (isLoggable(Level.FINER)) {
            LogRecord lr = new LogRecord(Level.FINER, msg);
            doLog(lr);
        }
    }