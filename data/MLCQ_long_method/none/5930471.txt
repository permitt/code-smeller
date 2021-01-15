    public void threadSingletonServiceAdded(@Observes ComponentAdded<ThreadSingletonService> componentAdded) {
        if (componentAdded.getComponent() != this) {
            return;
        }

        contextThreadListener = new OWBContextThreadListener();
        ThreadContext.addThreadContextListener(contextThreadListener);
    }