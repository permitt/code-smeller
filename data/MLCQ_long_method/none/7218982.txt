    @SuppressWarnings("unchecked")
    @Override
    public T call() throws Exception {
        return ((Callable<T>)source).call();
    }