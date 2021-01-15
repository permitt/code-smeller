  public void resolve()
  {
    XSDSchemaPrefixRenamer xsdSchemaPrefixRenamer = new XSDSchemaPrefixRenamer();
    xsdSchemaPrefixRenamer.visitSchema(xsdSchema);
  }