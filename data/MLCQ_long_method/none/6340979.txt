    @Override
    public void addPages() {
        page = new WizardNewFileCreationPage("newSuppressionPage", selection); //$NON-NLS-1$
        page.setTitle(Messages.getString("NewSuppressionWizard.NewWizard_title")); //$NON-NLS-1$
        page.setDescription(Messages.getString("NewSuppressionWizard.NewWizard_description")); //$NON-NLS-1$
        page.setImageDescriptor(AbstractUIPlugin.imageDescriptorFromPlugin(ValgrindEditorPlugin.PLUGIN_ID, "icons/newsupp_wiz.png")); //$NON-NLS-1$
        page.setFileExtension(EXT_SUPP);
        addPage(page);
    }