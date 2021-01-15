  public TestHttpServletRequest(String queryString) {
    this.queryString = queryString;
    this.content = new byte[0];
    this.contentType = null;
    this.characterEncoding = null;
    decodeParams();
  }