    @Override
    public void saw(T element) {
      long thisElementIndex = nextElementIndex;
      nextElementIndex++;
      if (thisElementIndex == nextIndexToReport) {
        nextIndexToReport = nextElementIndex;
        report(element);
      }
    }