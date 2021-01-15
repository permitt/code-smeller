  @Override
  public TStatus getStatus(long tid) {
    verifyReserved(tid);
    return _getStatus(tid);
  }