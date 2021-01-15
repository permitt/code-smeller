  private void addConfigPropertyToXML(String name, String value) {
    if (configuration().containsKey(name)) {
      pluginElement.getSingleChild("configuration").getSingleChild(name).setText(value);
    } else if (configuration.isEmpty()) {
      pluginElement.appendChild(createElement("configuration", createElement(name, value)));
    } else {
      pluginElement.getSingleChild("configuration").appendChild(createElement(name, value));
    }
  }