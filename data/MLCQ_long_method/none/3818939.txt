   public InMemoryDirectoryServiceFactory() {
      try {
         directoryService = new DefaultDirectoryService();
      } catch (Exception e) {
         throw new RuntimeException(e);
      }
      directoryService.setShutdownHookEnabled(false);
      partitionFactory = new AvlPartitionFactory();
   }