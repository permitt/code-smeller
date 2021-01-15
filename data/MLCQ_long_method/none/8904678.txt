  public boolean isSet(_Fields field) {
    if (field == null) {
      throw new IllegalArgumentException();
    }

    switch (field) {
    case NS:
      return isSetNs();
    }
    throw new IllegalStateException();
  }