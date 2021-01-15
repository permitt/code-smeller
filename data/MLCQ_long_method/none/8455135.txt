    public GoraEndpoint(final String uri,
                        final GoraComponent goraComponent,
                        final GoraConfiguration config,
                        final DataStore<Object, Persistent> dataStore) {

        super(uri, goraComponent);
        this.configuration = config;
        this.dataStore = dataStore;
    }