  public void setPositionExt(GphotoPosition positionExt) {
    if (positionExt == null) {
      removeExtension(GphotoPosition.class);
    } else {
      setExtension(positionExt);
    }
  }