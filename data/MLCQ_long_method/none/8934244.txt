    public boolean isSet(_Fields field) {
      if (field == null) {
        throw new IllegalArgumentException();
      }

      switch (field) {
      case O1:
        return isSetO1();
      case O2:
        return isSetO2();
      }
      throw new IllegalStateException();
    }