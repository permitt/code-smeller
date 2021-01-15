    public static boolean isTrue(boolean expression) {
        // succeed as quickly as possible
        if (expression) {
            return true;
        }
        return isTrue(expression, "");//$NON-NLS-1$
    }