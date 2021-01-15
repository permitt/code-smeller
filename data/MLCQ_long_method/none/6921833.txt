  public void setCommentCount(Integer commentCount) {
    if (commentCount != null) {
      setExtension(new GphotoCommentCount(commentCount));
    } else {
      removeExtension(GphotoCommentCount.class);
    }
  }