    UnifiedHLImpl(final UnifiedHighlighter.OffsetSource offsetSource) {
      this.offsetSource = offsetSource;
      maxPassages = new int[hlFields.size()];
      Arrays.fill(maxPassages, maxFrags);
    }