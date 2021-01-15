  private void printCommaUnlessFirst() {
    if (!isFirst) {
      stream.print(",");
    }
    isFirst = false;
  }