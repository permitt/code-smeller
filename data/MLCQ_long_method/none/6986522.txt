  public SynchronizedStatement(SourcePosition sourcePosition, Expression expression, Block body) {
    super(sourcePosition);
    this.expression = checkNotNull(expression);
    this.body = checkNotNull(body);
  }