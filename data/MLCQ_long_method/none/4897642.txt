  @Override
  public void getDictionaryIds(int[] inDocIds, int inStartPos, int inDocIdsSize, int[] outDictionaryIds,
      int outStartPos) {
    _reader.readValues(inDocIds, inStartPos, inDocIdsSize, outDictionaryIds, outStartPos);
  }