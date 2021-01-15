  public int compareColumnQualifier(Text cq) {
    return WritableComparator.compareBytes(colQualifier, 0, colQualifier.length, cq.getBytes(), 0,
        cq.getLength());
  }