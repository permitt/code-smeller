    ClosureType toNonNullable() {
      return isNullable() ? new ClosureBangDecoratedType(this) : this;
    }