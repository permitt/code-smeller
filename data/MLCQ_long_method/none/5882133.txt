    @Inject
    public CandidateIdFilter( final EntityCollectionManagerFactory entityCollectionManagerFactory,
                              final EntityIndexFactory entityIndexFactory,
                              final IndexLocationStrategyFactory indexLocationStrategyFactory,
                              final IndexProducer indexProducer) {
        this.entityCollectionManagerFactory = entityCollectionManagerFactory;
        this.entityIndexFactory = entityIndexFactory;
        this.indexLocationStrategyFactory = indexLocationStrategyFactory;
        this.indexProducer = indexProducer;
    }