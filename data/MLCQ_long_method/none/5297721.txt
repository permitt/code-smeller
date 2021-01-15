  public BufferedProtocolReadToWrite(StructType thriftType, FieldIgnoredHandler errorHandler) {
    super();
    this.thriftType = thriftType;
    this.errorHandler = errorHandler;
  }