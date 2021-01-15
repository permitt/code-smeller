  @Provides
  @Parameter("fields")
  static Optional<String> provideFields(HttpServletRequest req) {
    return extractOptionalParameter(req, ListObjectsAction.FIELDS_PARAM);
  }