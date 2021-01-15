  public static GphotoId from(Long id) {
    return new GphotoId(id == null ? null : Long.toString(id));
  }