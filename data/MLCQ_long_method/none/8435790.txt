    public MethodNotFoundException(Object pojo, String methodName, Throwable cause) {
        super("Method with name: " + methodName + " not found on bean: " + pojo + " of type:" + ObjectHelper.className(pojo), null, cause);
        this.methodName = methodName;
        this.bean = pojo;
    }