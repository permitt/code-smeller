  public static final JsPromiseError create(final Throwable e) {
    if (e == null) {
      return create();
    } else {
      return createFromThrowable(e);
    }
  }