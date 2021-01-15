  @Override
  public void recordAllocBytes(long bytesUsed, long bytesAllocated) {
    incrCounter(LlapIOCounters.ALLOCATED_USED_BYTES, bytesUsed);
    incrCounter(LlapIOCounters.ALLOCATED_BYTES, bytesAllocated);
  }