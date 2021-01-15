    private void init(Class<?> interfaceClass, Object interfaceInstance) {
        /**
         * The interface this server implements.
         */
        this.interfaceInstance = interfaceInstance;
        this.serviceDescription = new ServiceDescription(interfaceClass);
    }