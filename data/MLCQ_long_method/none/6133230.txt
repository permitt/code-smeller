	@Override
	protected void addUserInputPages() {
		String initialSetting = getNameUpdating().getCurrentElementName();
		RenameInputWizardPage inputPage = createInputPage(fInputPageDescription,
				initialSetting);
		inputPage.setImageDescriptor(fInputPageImageDescriptor);
		addPage(inputPage);
	}