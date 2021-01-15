    @Override
    public boolean releaseCheckpoint(String checkpoint) {
        log.info("Released checkpoint [{}]", checkpoint);
        return store.release(checkpoint);
    }