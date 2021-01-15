public class ContainerEnvironmentVariableDialog extends Dialog {

	private final EnvironmentVariableModel model;

	private final DataBindingContext dbc = new DataBindingContext();

	public ContainerEnvironmentVariableDialog(final Shell parentShell) {
		super(parentShell);
		this.model = new EnvironmentVariableModel();
	}

	public ContainerEnvironmentVariableDialog(final Shell parentShell,
			final EnvironmentVariableModel selectedVariable) {
		super(parentShell);
		this.model = new EnvironmentVariableModel(selectedVariable);
	}

	@Override
	protected void configureShell(final Shell shell) {
		super.configureShell(shell);
		setShellStyle(getShellStyle() | SWT.RESIZE);
		shell.setText(WizardMessages
				.getString("ContainerEnvironmentVariableDialog.title")); //$NON-NLS-1$
	}

	@Override
	protected Point getInitialSize() {
		return new Point(400, super.getInitialSize().y);
	}

	/**
	 * Disable the 'OK' button by default
	 */
	@Override
	protected Button createButton(Composite parent, int id, String label,
			boolean defaultButton) {
		final Button button = super.createButton(parent, id, label,
				defaultButton);
		if (id == IDialogConstants.OK_ID) {
			button.setEnabled(false);
		}
		return button;
	}

	@Override
	protected Control createDialogArea(Composite parent) {
		final int COLUMNS = 2;
		final Composite container = new Composite(parent, SWT.NONE);
		GridDataFactory.fillDefaults().align(SWT.FILL, SWT.FILL)
				.span(COLUMNS, 1).grab(true, true).applyTo(container);
		GridLayoutFactory.fillDefaults().numColumns(COLUMNS).margins(10, 10)
				.applyTo(container);
		final Label explanationLabel = new Label(container, SWT.NONE);
		explanationLabel.setText(WizardMessages.getString(
				"ContainerEnvironmentVariableDialog.explanationLabel")); //$NON-NLS-1$
		GridDataFactory.fillDefaults().align(SWT.FILL, SWT.CENTER)
				.span(COLUMNS, 1).grab(false, false).applyTo(explanationLabel);
		final Label variableNameLabel = new Label(container, SWT.NONE);
		variableNameLabel.setText(WizardMessages
				.getString("ContainerEnvironmentVariableDialog.nameLabel")); //$NON-NLS-1$
		GridDataFactory.fillDefaults().align(SWT.FILL, SWT.CENTER)
				.grab(false, false).applyTo(variableNameLabel);
		final Text variableNameText = new Text(container, SWT.BORDER);
		GridDataFactory.fillDefaults().align(SWT.FILL, SWT.CENTER)
				.grab(true, false).applyTo(variableNameText);
		final Label variableValueLabel = new Label(container, SWT.NONE);
		variableValueLabel.setText(WizardMessages
				.getString("ContainerEnvironmentVariableDialog.valueLabel")); //$NON-NLS-1$
		GridDataFactory.fillDefaults().align(SWT.FILL, SWT.CENTER)
				.grab(false, false).applyTo(variableValueLabel);
		final Text variableValueText = new Text(container, SWT.BORDER);
		GridDataFactory.fillDefaults().align(SWT.FILL, SWT.CENTER)
				.grab(true, false).applyTo(variableValueText);
		// error message
		final Label errorMessageLabel = new Label(container, SWT.NONE);
		GridDataFactory.fillDefaults().align(SWT.FILL, SWT.CENTER)
				.span(COLUMNS, 1).grab(true, false).applyTo(errorMessageLabel);

		// listening to changes
		final ISWTObservableValue variableNameObservable = WidgetProperties
				.text(SWT.Modify).observe(variableNameText);
		dbc.bindValue(variableNameObservable,
				BeanProperties.value(EnvironmentVariableModel.class,
						EnvironmentVariableModel.NAME).observe(model));
		final ISWTObservableValue variableValueObservable = WidgetProperties
				.text(SWT.Modify).observe(variableValueText);
		dbc.bindValue(variableValueObservable,
				BeanProperties.value(EnvironmentVariableModel.class,
						EnvironmentVariableModel.VALUE).observe(model));

		variableNameObservable
				.addValueChangeListener(onEnvironmentVariableSettingsChanged());
		variableValueObservable
				.addValueChangeListener(onEnvironmentVariableSettingsChanged());
		return container;
	}

	private IValueChangeListener onEnvironmentVariableSettingsChanged() {
		return event -> validateInput();
	}

	private void validateInput() {
		final String variableName = model.getName();
		final String variableValue = model.getValue();
		if (variableName == null || variableName.isEmpty()
				|| variableValue == null || variableValue.isEmpty()) {
			setOkButtonEnabled(false);
		} else {
			setOkButtonEnabled(true);
		}
	}

	private void setOkButtonEnabled(final boolean enabled) {
		getButton(IDialogConstants.OK_ID).setEnabled(enabled);
	}

	public EnvironmentVariableModel getEnvironmentVariable() {
		return new EnvironmentVariableModel(model.getName(), model.getValue());
	}

}