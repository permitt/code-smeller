  public void setStackTraceTexts(String[] texts) {
    if (texts == null) {
      this.texts = null;
    } else {
      this.texts = texts.clone();
    }
  }