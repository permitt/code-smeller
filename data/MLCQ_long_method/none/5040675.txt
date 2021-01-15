    @Override
    public void sync() {
        if ( dirty )
            writeState();
    }