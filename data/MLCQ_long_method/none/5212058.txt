  @Override
  public void close() throws IOException {
    // This will flush any unsent documents.
    commit();
    // close the client
    if (client != null) {
      client.shutdown();
    }
  }