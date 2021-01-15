	@Override
	public void releaseContributions(ContributionManager mgr) {
		if (mgr instanceof MenuManager) {
			MenuManager menu = (MenuManager) mgr;
			releaseContributionManager(menu);
		} else if (mgr instanceof ToolBarManager) {
			ToolBarManager toolbar = (ToolBarManager) mgr;
			releaseContributionManager(toolbar);
		} else {
			WorkbenchPlugin.log("releaseContributions: Unhandled manager: " + mgr); //$NON-NLS-1$
		}
	}