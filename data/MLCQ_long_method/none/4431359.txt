    @Override
    protected Collection<IPZoneEntity> loadFromService(ISecurityDataEnrichServiceClient client) {
        return client.listIPZones();
    }