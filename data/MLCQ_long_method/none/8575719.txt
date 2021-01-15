  public AuthenticationKey(int keyId, long expirationDate, SecretKey key) {
    this.id = keyId;
    this.expirationDate = expirationDate;
    this.secret = key;
  }