  public static void putAll(Map<String, String> additionalEnvironment) {
    Map<String, String> environment = new HashMap<String, String>(System.getenv());
    environment.putAll(additionalEnvironment);
    updateEnvironment(environment);
  }