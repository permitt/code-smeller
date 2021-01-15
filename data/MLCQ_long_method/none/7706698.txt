    public RaveError(Class<?> clazz, String item, String errorMsg) {
        this.clazz = clazz;
        this.errorMsg = errorMsg;
        classElement = item;
    }