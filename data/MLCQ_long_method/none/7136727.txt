  @Override
  public Map<String, Object> getRequestContextLocalAttrs()
  {
    return Collections.unmodifiableMap(_context.getRawRequestContext().getLocalAttrs());
  }