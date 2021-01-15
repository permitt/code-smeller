    protected RexNode makeMultiply(
        RexNode a,
        RexNode b) {
      return builder.makeCall(
          SqlStdOperatorTable.MULTIPLY,
          a,
          b);
    }