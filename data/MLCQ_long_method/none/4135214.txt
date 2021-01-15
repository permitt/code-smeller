      public boolean hasNext() {
        if (firstCall) {
          initializeMapping();
          firstCall = false;
        } else {
          computeNextMapping(iterationIdx.length - 1);
        }
        return nextMapping != null;
      }