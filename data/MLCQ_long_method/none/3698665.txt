    public Self addExceptionHandler(GenericExceptionHandler<Input, Output> handler) {
        exceptionHandlers.add(handler);
        return getThis();
    }