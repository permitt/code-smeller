public class RegexpEntryDialog extends Dialog {
	private static final String TITLE = "Regular expression";

	private final String title;
	private String entry;
	private Label entryLabel;
	private Text entryText;
	private Label errorLabel;

	public RegexpEntryDialog(final Shell shell) {
		super(shell);
		this.title = TITLE;
		entry = "";
	}

	public String getEntry() {
		return entry;
	}

	public void setEntry(final String entry) {
		this.entry = entry;
	}

	@Override
	protected int getShellStyle() {
		return super.getShellStyle() | SWT.RESIZE;
	}

	@Override
	protected void configureShell(final Shell newShell) {
		super.configureShell(newShell);
		if (title != null) {
			newShell.setText(title);
		}
	}

	private void validate(final String newText) {
		try {
			Pattern.compile(newText);
			errorLabel.setVisible(false);

			Button button = getButton(IDialogConstants.OK_ID);
			if (button != null) {
				button.setEnabled(true);
			}
		} catch (PatternSyntaxException e) {
			errorLabel.setVisible(true);
			Button button = getButton(IDialogConstants.OK_ID);
			if (button != null) {
				button.setEnabled(false);
			}
		}
	}

	@Override
	protected void okPressed() {
		entry = entryText.getText();

		super.okPressed();
	}

	@Override
	protected Control createDialogArea(final Composite parent) {
		Composite container = (Composite) super.createDialogArea(parent);
		container.setLayout(new GridLayout(1, false));
		container.setLayoutData(new GridData(GridData.FILL_BOTH));

		Composite panel = new Composite(container, SWT.NONE);
		GridLayout layout = new GridLayout(3, false);
		panel.setLayout(layout);
		panel.setLayoutData(new GridData(GridData.FILL_HORIZONTAL));

		createNameArea(panel);

		Dialog.applyDialogFont(container);
		validate("");
		return container;
	}

	protected void createNameArea(final Composite parent) {
		Label label = new Label(parent, SWT.NONE);
		label.setLayoutData(new GridData(GridData.HORIZONTAL_ALIGN_BEGINNING));
		label.setToolTipText("tooltip");

		entryLabel = new Label(parent, SWT.NONE);
		entryLabel.setText("text");
		entryLabel.setLayoutData(new GridData(GridData.HORIZONTAL_ALIGN_BEGINNING));
		entryLabel.setToolTipText("tooltip");

		entryText = new Text(parent, SWT.SINGLE | SWT.BORDER);
		entryText.setLayoutData(new GridData(GridData.FILL_HORIZONTAL));
		entryText.setText(entry);
		entryText.addModifyListener(new ModifyListener() {

			@Override
			public void modifyText(final ModifyEvent e) {
				validate(entryText.getText());
			}
		});

		entryLabel.setSize(entryLabel.getSize().x, entryText.getSize().y);

		errorLabel = new Label(parent, SWT.NONE);
		errorLabel.setText("error");
		errorLabel.setLayoutData(new GridData(GridData.HORIZONTAL_ALIGN_BEGINNING));
		errorLabel.setToolTipText("error tooltip");
		errorLabel.setVisible(false);
	}
}