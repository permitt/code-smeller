	private MCoreExpression createVisibleWhen() {
		if (visibleWhen == null) {
			return null;
		}
		MCoreExpression exp = UiFactoryImpl.eINSTANCE.createCoreExpression();
		exp.setCoreExpressionId("programmatic." + MenuHelper.getId(configElement)); //$NON-NLS-1$
		exp.setCoreExpression(visibleWhen);
		return exp;
	}