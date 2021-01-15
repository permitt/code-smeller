    private void recomputeHeight() {
      this.height = 1 + Math.max(height(left), height(right));
    }