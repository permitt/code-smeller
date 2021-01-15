  public void severe(String msg, Object... params) {
    if (isSevereEnabled()) {
      CallerDetails details = inferCaller();
      logger.logp(Level.SEVERE, details.clazz, details.method, msg, params);
    }
  }