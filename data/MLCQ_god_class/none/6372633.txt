public class WizardShortcutAction extends Action implements IPluginContribution {
	private IWizardDescriptor descriptor;

	private IWorkbenchWindow window;

	/**
	 *
	 * @param aWindow
	 *            The window to use for the shell and selection service.
	 * @param aDescriptor
	 *            The descriptor with information for triggering the desired
	 *            wizard.
	 */
	public WizardShortcutAction(IWorkbenchWindow aWindow,
			IWizardDescriptor aDescriptor) {
		super(aDescriptor.getLabel());
		descriptor = aDescriptor;
		setToolTipText(descriptor.getDescription());
		setImageDescriptor(descriptor.getImageDescriptor());
		setId(ActionFactory.NEW.getId());
		this.window = aWindow;
	}

	/**
	 * This action has been invoked by the user
	 */
	@Override
	public void run() {
		// create instance of target wizard

		IWorkbenchWizard wizard;
		try {
			wizard = descriptor.createWizard();
		} catch (CoreException e) {
			ErrorDialog.openError(window.getShell(),
					CommonNavigatorMessages.NewProjectWizard_errorTitle,
					CommonNavigatorMessages.NewProjectAction_text, e
							.getStatus());
			return;
		}

		ISelection selection = window.getSelectionService().getSelection();

		if (selection instanceof IStructuredSelection) {
			wizard
					.init(window.getWorkbench(),
							(IStructuredSelection) selection);
		} else {
			wizard.init(window.getWorkbench(), StructuredSelection.EMPTY);
		}

		if(descriptor.canFinishEarly() && !descriptor.hasPages()) {
			wizard.performFinish();
		} else {
			Shell parent = window.getShell();
			WizardDialog dialog = new WizardDialog(parent, wizard);
			dialog.create();
			// PlatformUI.getWorkbench().getHelpSystem().setHelp(dialog.getShell(),
			// IWorkbenchHelpContextIds.NEW_WIZARD_SHORTCUT);
			dialog.open();
		}
	}

	@Override
	public String getLocalId() {
		return descriptor.getId();
	}

	@Override
	public String getPluginId() {
		return descriptor.getId();
	}

}