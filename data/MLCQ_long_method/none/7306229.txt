    public void setServiceHost(final IBuildServiceHost value) {
        serviceHost = value;

        if (serviceHost != null) {
            getWebServiceObject().setServiceHostUri(serviceHost.getURI());
        } else {
            getWebServiceObject().setServiceHostUri(null);
        }
    }