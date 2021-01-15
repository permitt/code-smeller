  @Override
  public InputStream getInputStream() throws IOException {
    return new FileInputStream(file);
  }