  public DataBlockEncoder getEncoder() {
    if (encoder == null && id != 0) {
      // lazily create the encoder
      encoder = createEncoder(encoderCls);
    }
    return encoder;
  }