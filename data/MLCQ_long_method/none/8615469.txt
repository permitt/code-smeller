    ClientCacheQueryResponse(long requestId, ClientCacheQueryCursor cursor) {
        super(requestId);

        assert cursor != null;

        this.cursor = cursor;
    }