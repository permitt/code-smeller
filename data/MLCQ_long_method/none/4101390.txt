    @Override
    public <T> Set<ConstraintViolation<T>> validateParameters(T object, Method method, Object[] parameterValues,
        Class<?>... groups) {
        return validationJobFactory.validateParameters(object, method, parameterValues, groups).getResults();
    }