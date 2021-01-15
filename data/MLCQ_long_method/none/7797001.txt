  @Override
  public String composeName(String name, String prefix) throws NamingException {
    checkIsDestroyed();
    return composeName(nameParser.parse(name), nameParser.parse(prefix)).toString();
  }