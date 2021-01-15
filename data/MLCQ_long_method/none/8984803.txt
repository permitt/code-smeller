  public int maxDoc() {
    if (this.maxDoc == -1) {
      throw new IllegalStateException("maxDoc isn't set yet");
    }
    return maxDoc;
  }