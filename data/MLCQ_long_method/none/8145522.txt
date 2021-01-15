  public boolean needsTychoBuild() {
    return (this.needsMavenBuild() && this.runtimeProject.isEclipsePluginProject());
  }