    @Override
    public <R> Promise<R> put(Entity<?> entity, Class<R> aClass) {
        return method(HttpMethod.PUT, entity, aClass);
    }