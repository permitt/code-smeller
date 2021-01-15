    @Override
    public <A> GraphTraversalSource withSideEffect(final String key, final Supplier<A> initialValue, final BinaryOperator<A> reducer) {
        return (GraphTraversalSource) TraversalSource.super.withSideEffect(key, initialValue, reducer);
    }