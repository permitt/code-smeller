    public static boolean isDeprecated(TypeMirror baseType) {
        if (baseType instanceof DeclaredType) {
            return isDeprecated((TypeElement) ((DeclaredType) baseType).asElement());
        }
        return false;
    }