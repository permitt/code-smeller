    public Object getFieldValue(_Fields field) {
      switch (field) {
      case SUCCESS:
        return getSuccess();

      case CS_EXCEPTION:
        return getCsException();

      }
      throw new IllegalStateException();
    }