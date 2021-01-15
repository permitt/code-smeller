  public AvaticaStatement newStatement(AvaticaConnection connection,
      Meta.StatementHandle h, int resultSetType, int resultSetConcurrency,
      int resultSetHoldability) {
    return new AvaticaJdbc41Statement(connection, h, resultSetType,
        resultSetConcurrency, resultSetHoldability);
  }