   @Override
   public void initializeDocument( final JCas documentValue ) {
      _instance = 1;
      final SourceData sourceData = SourceMetadataUtil.getSourceData( documentValue );
      if ( sourceData == null ) {
         LOGGER.warn( "No document source data." );
         setEmptyDocInfo();
         return;
      }
      try {
         _encounter = SourceMetadataUtil.getEncounterNum( sourceData );
         _provider = SourceMetadataUtil.getProviderId( sourceData );
         _start = SourceMetadataUtil.getStartDate( sourceData );
      } catch ( ResourceProcessException rpE ) {
         LOGGER.warn( "Error setting document source data: " + rpE.getMessage() );
         setEmptyDocInfo();
      }
   }