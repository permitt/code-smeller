  default BooleanConsumer andThen(BooleanConsumer after) {
    Objects.requireNonNull(after);
    return (boolean t) -> { accept(t); after.accept(t); };
  }