    @Override
    public CODE<T> a(String selector, String href, String anchorText) {
      return setSelector(a(), selector).$href(href)._(anchorText)._();
    }