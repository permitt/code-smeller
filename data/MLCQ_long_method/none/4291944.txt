    DependentBeanEntry(T instance, Bean<?> bean, CreationalContext<T> creationalContext)
    {
        this.instance = instance;
        this.bean = bean;
        this.creationalContext = creationalContext;
    }