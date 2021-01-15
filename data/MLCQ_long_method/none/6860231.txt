  @Override
  public void dispose() {
    database.removeListener(listener);
  }