    public PrepareSource(String tag, MediaSource mediaSource, boolean resetPosition,
        boolean resetState) {
      super(tag, "PrepareSource");
      this.mediaSource = mediaSource;
      this.resetPosition = resetPosition;
      this.resetState = resetState;
    }