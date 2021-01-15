    @Override
    protected Endpoint createEndpoint(String uri, String remaining, Map<String, Object> parameters) throws Exception {
        BeanValidatorEndpoint endpoint = new BeanValidatorEndpoint(uri, this);
        endpoint.setLabel(remaining);
        setProperties(endpoint, parameters);
        return endpoint;
    }