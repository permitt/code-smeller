    @Override
    public CloseableIteration<BindingSet, QueryEvaluationException> evaluate(BindingSet bindings)
            throws QueryEvaluationException {
        return evaluate(Collections.singleton(bindings));
    }