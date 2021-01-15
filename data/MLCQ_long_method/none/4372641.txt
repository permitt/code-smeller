    public void clientCreated(Client client) {
        for (ClientLifeCycleListener listener : listeners) {
            listener.clientCreated(client);
        }
    }