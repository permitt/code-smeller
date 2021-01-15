  public static <T, TResult> Queryable<TResult> selectManyN(Queryable<T> source,
      FunctionExpression<Function2<T, Integer, Enumerable<TResult>>> selector) {
    throw Extensions.todo();
  }