    @Override
    public String getNameAndSignature() {
        String className = method.getDeclaringClass().getName();
        return className + "." + method.getName() + method.getSignature().toMethodDescriptor();
    }