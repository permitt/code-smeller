  @Override
  public void close() throws IOException {
    IOUtils.cleanup(null, src);
    factory.close();
  }