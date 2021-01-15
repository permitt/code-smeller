	private void createMenuEntries(Menu menu, DisplayItem parent,
			boolean trackDynamics) {
		if (menu == null)
			return;
		MenuItem[] menuItems = menu.getItems();

		Map findDynamics = new HashMap();
		DynamicContributionItem dynamicEntry = null;

		if (trackDynamics && menu.getParentItem() != null) {
			//Search for any dynamic menu entries which will be handled later
			Object data = menu.getParentItem().getData();
			if (data instanceof IContributionManager) {
				IContributionManager manager = (IContributionManager) data;
				IContributionItem[] items = manager.getItems();
				for (int i = 0; i < items.length; i++) {
					if (items[i].isDynamic()) {
						findDynamics.put(i > 0 ? items[i - 1] : null, items[i]);
					}
				}

				//If there is an item with no preceeding item, set it up to be
				//added first.
				if (findDynamics.containsKey(null)) {
					IContributionItem item = (IContributionItem) findDynamics
							.get(null);
					dynamicEntry = new DynamicContributionItem(item);
					parent.addChild(dynamicEntry);
				}
			}
		}

		for (int i = 0; i < menuItems.length; i++) {
			if (!menuItems[i].getText().equals("")) { //$NON-NLS-1$
				IContributionItem contributionItem =
						(IContributionItem) menuItems[i].getData();
				if (dynamicEntry != null
						&& contributionItem.equals(dynamicEntry
								.getIContributionItem())) {
					//If the last item added is the item meant to go before the
					//given dynamic entry, add the dynamic entry so it is in the
					//correct order.
					dynamicEntry.addCurrentItem(menuItems[i]);
				} else {
					DisplayItem menuEntry = new DisplayItem(
							menuItems[i].getText(), contributionItem);

					Image image = menuItems[i].getImage();
					if (image != null) {
						menuEntry.setImageDescriptor(ImageDescriptor
								.createFromImage(image));
					}
					menuEntry.setActionSet((ActionSet) idToActionSet
							.get(getActionSetID(contributionItem)));
					parent.addChild(menuEntry);

					if (ActionFactory.NEW.getId()
							.equals(((IContributionItem) menuItems[i].getData())
									.getId())) {
						initializeNewWizardsMenu(menuEntry);
						wizards = menuEntry;
					} else if (SHORTCUT_CONTRIBUTION_ITEM_ID_OPEN_PERSPECTIVE
							.equals(((IContributionItem) menuItems[i].getData())
									.getId())) {
						initializePerspectivesMenu(menuEntry);
						perspectives = menuEntry;
					} else if (SHORTCUT_CONTRIBUTION_ITEM_ID_SHOW_VIEW
							.equals(((IContributionItem) menuItems[i].getData())
									.getId())) {
						initializeViewsMenu(menuEntry);
						views = menuEntry;
					} else {
						createMenuEntries(menuItems[i].getMenu(), menuEntry,
								trackDynamics);
					}

					if (menuEntry.getChildren().isEmpty()) {
						menuEntry
								.setCheckState(getMenuItemIsVisible(menuEntry));
					}

					if (image == null) {
						if (parent != null && parent.getParent() == null) {
							menuEntry.setImageDescriptor(menuImageDescriptor);
						} else if (menuEntry.getChildren().size() > 0) {
							menuEntry
									.setImageDescriptor(submenuImageDescriptor);
						}
					}
				}
				if (trackDynamics
						&& findDynamics.containsKey(menuItems[i].getData())) {
					IContributionItem item = (IContributionItem) findDynamics
							.get(menuItems[i].getData());
					dynamicEntry = new DynamicContributionItem(item);
					dynamicEntry
							.setCheckState(getMenuItemIsVisible(dynamicEntry));
					parent.addChild(dynamicEntry);
				}
			}
		}
	}