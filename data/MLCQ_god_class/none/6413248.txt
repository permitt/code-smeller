public abstract class AbstractEvaluationHandler extends AbstractEnabledHandler {
	private static final String PROP_ENABLED = "enabled"; //$NON-NLS-1$
	private IEvaluationService evaluationService;
	private IPropertyChangeListener enablementListener;
	private IEvaluationReference enablementRef;

	protected IEvaluationService getEvaluationService() {
		if (evaluationService == null) {
			evaluationService = PlatformUI.getWorkbench()
					.getService(IEvaluationService.class);
		}
		return evaluationService;
	}

	protected void registerEnablement() {
		enablementRef = getEvaluationService().addEvaluationListener(
				getEnabledWhenExpression(), getEnablementListener(),
				PROP_ENABLED);
	}

	protected abstract Expression getEnabledWhenExpression();

	/**
	 * @return
	 */
	private IPropertyChangeListener getEnablementListener() {
		if (enablementListener == null) {
			enablementListener = event -> {
				if (event.getProperty() == PROP_ENABLED) {
					if (event.getNewValue() instanceof Boolean) {
						setEnabled(((Boolean) event.getNewValue())
								.booleanValue());
					} else {
						setEnabled(false);
					}
				}
			};
		}
		return enablementListener;
	}

	@Override
	public void dispose() {
		if (enablementRef != null) {
			evaluationService.removeEvaluationListener(enablementRef);
			enablementRef = null;
			enablementListener = null;
			evaluationService = null;
		}
		super.dispose();
	}
}