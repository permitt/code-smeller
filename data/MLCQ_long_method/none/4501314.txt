    protected MetaDataReader(File logFile, int logFileID) throws IOException {
      this.logFile = logFile;
      metaDataFile = Serialization.getMetaDataFile(logFile);
      this.logFileID = logFileID;
    }