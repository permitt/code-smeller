  synchronized void removeSegment(DataSegment segment)
  {
    if (segments.remove(segment)) {
      currSize -= segment.getSize();
    }
  }