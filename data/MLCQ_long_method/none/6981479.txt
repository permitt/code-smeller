  @Override
  public ProjectConfig loadConfiguration(String configFilename) throws InvalidProject {
    return parse(projectConfigs.get(configFilename));
  }