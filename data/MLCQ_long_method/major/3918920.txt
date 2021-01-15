    public void removeDependentService(
        CachingServiceReference<?> serviceReference) {

        _dependentServices.remove(serviceReference);
    }