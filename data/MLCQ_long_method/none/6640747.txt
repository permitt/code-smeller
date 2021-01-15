  public static void d(String tag, Throwable tr, String msg, Object... args) {
    if (sHandler.isLoggable(DEBUG)) {
      d(tag, formatString(msg, args), tr);
    }
  }