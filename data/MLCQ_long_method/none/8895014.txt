  public void addToAborted(long elem) {
    if (this.aborted == null) {
      this.aborted = new HashSet<Long>();
    }
    this.aborted.add(elem);
  }