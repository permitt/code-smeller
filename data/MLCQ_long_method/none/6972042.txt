  public static <E> SortedSetTestSuiteBuilder<E> using(TestSortedSetGenerator<E> generator) {
    SortedSetTestSuiteBuilder<E> builder = new SortedSetTestSuiteBuilder<E>();
    builder.usingGenerator(generator);
    return builder;
  }