  @XmlElementWrapper(name = "references")
  @XmlElement(name = "reference")
  public List<ReferenceResource> getReferenceResources()
  {
    return referenceResources;
  }