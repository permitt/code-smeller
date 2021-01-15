    protected void getAllContributedActions(HashSet set, IContributionItem item) {
        if (item instanceof MenuManager) {
			for (IContributionItem subItem : ((MenuManager) item).getItems()) {
				getAllContributedActions(set, subItem);
			}
        } else if (item instanceof ActionContributionItem) {
            set.add(((ActionContributionItem) item).getAction());
        }
    }