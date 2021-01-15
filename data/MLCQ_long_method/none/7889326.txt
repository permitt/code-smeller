    @Override
    public <T> Optional<T> createOptional(ValueTypeInfo<T> innerType) throws IOException {
      if (stream.readBoolean()) {
        return Optional.of(innerType.createNotNull(this));
      }
      return Optional.empty();
    }