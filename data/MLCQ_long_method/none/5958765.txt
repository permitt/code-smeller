    @Managed
    public void flush() {
        stats.flushes.record();
        poolVersion.incrementAndGet();
    }