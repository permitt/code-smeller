	@Override
	protected Control createContents(Composite parent) {

		Composite composite = SWTUtils.createHVFillComposite(parent,
				SWTUtils.MARGINS_NONE);

		SWTUtils.createLabel(composite, UIText.DecoratorPreferencesPage_description);

		Composite folderComposite = SWTUtils.createHFillComposite(composite,
				SWTUtils.MARGINS_NONE);

		TabFolder tabFolder = new TabFolder(folderComposite, SWT.NONE);
		tabFolder.setLayoutData(SWTUtils.createHVFillGridData());

		tabFolder.addSelectionListener(new SelectionAdapter() {

			@Override
			public void widgetSelected(SelectionEvent e) {
				if (navigatorPreview != null && changeSetPreview != null) {
					if (UIText.DecoratorPreferencesPage_otherDecorations.equals(e.item.getData())) {
						navigatorPreview.hide();
						changeSetPreview.show();
					} else {
						changeSetPreview.hide();
						navigatorPreview.show();
					}
				}
			}

		});

		changeSetPreview = new ChangeSetPreview(composite);
		navigatorPreview = new NavigatorPreview(composite);

		generalTab = new GeneralTab(tabFolder);
		textDecorationTab = new TextDecorationTab(tabFolder);
		iconDecorationTab = new IconDecorationTab(tabFolder);
		otherDecorationTab = new OtherDecorationTab(tabFolder);

		initializeValues();

		changeSetPreview.hide();

		changeSetPreview.refresh();
		navigatorPreview.refresh();

		generalTab.addObserver(navigatorPreview);
		textDecorationTab.addObserver(navigatorPreview);
		iconDecorationTab.addObserver(navigatorPreview);

		otherDecorationTab.addObserver(changeSetPreview);

		// TODO: Add help text for this preference page

		themeListener = new IPropertyChangeListener() {
			@Override
			public void propertyChange(PropertyChangeEvent event) {
				navigatorPreview.refresh();
				changeSetPreview.refresh();
			}
		};
		PlatformUI.getWorkbench().getThemeManager().addPropertyChangeListener(
				themeListener);

		uiPrefsListener = new IPropertyChangeListener() {
			@Override
			public void propertyChange(PropertyChangeEvent event) {
				String property = event.getProperty();
				if (UIPreferences.DATE_FORMAT.equals(property)
						|| UIPreferences.DATE_FORMAT_CHOICE.equals(property)) {
					changeSetPreview.refresh();
				}
			}
		};
		getPreferenceStore().addPropertyChangeListener(uiPrefsListener);

		Dialog.applyDialogFont(parent);

		return tabFolder;
	}