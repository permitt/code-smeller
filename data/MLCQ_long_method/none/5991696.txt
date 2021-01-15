    public void info(Supplier<String> msg) {
        if (log.isInfoEnabled()) {
            log.info(msg.get());
        }
    }