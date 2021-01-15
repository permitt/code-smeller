  public static LogicalExpression getIntervalDay(long intervalInMillis) {
      return new IntervalDayExpression(intervalInMillis);
  }