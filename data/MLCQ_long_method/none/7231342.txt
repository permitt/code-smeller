  @Implementation(minSdk = M)
  protected Network getActiveNetwork() {
    if (defaultNetworkActive) {
      return netIdToNetwork.get(getActiveNetworkInfo().getType());
    }
    return null;
  }