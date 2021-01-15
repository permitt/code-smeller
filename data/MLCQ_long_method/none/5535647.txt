  default V get(K key) {
    try {
      return getAsync(key).get();
    } catch (InterruptedException | ExecutionException e) {
      throw new SamzaException("GET failed for " + key, e);
    }
  }