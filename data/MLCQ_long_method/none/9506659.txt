  public ConnectionPoolId(final UserGroupInformation ugi, final String nnId,
      final Class<?> proto) {
    this.nnId = nnId;
    this.ugi = ugi;
    this.protocol = proto;
  }