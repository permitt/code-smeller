    @Override
    public void streamObjects(Consumer<Object> cons) {
      Object val = getObject();
      if (exists()) {
        cons.accept(val);
      }
    }