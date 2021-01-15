  @Override
  public void setIgnoreDepartedMembers(boolean ignore) {
    this.ignoreDepartedMembers = ignore;
    if (ignore) {
      setWaitOnExceptionFlag(true);
    }
  }