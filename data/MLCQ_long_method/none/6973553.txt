    @Override
    public void put(Range<K> range, V value) {
      checkArgument(
          subRange.encloses(range), "Cannot put range %s into a subRangeMap(%s)", range, subRange);
      TreeRangeMap.this.put(range, value);
    }