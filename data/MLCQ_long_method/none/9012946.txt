  @Override
  public String getInflectionForm(int wordId) {
    return inflFormDict[getLeftId(wordId)];
  }