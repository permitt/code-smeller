public class NullElementSelector implements ElementSelector, SelectorExt {

  @Override
  public String getLocalName() {
    return null;
  }

  @Override
  public String getNamespaceURI() {
    return null;
  }

  @Override
  public short getSelectorType() {
    return SAC_ELEMENT_NODE_SELECTOR;
  }

  @Override
  public String getElementName() {
    return null;
  }

  @Override
  public int getSpecificity() {
    return 0;
  }

  @Override
  public String[] getConstraints() {
    throw new UnsupportedOperationException();
  }

  @Override
  public String toString() {
    return "null selector";
  }

}