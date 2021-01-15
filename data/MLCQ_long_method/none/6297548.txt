    @Override
    public ByteBuffer getPayload()
    {
        if(!delegate.hasPayload()) {
            return null;
        }
        return delegate.getPayload().asReadOnlyBuffer();
    }