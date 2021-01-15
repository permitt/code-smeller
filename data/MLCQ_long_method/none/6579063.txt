    public void testDisableDecorator() {
        getDecoratorManager().clearCaches();
        definition.setEnabled(false);
        getDecoratorManager().updateForEnablementChange();
    }