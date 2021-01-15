	private void computeOverridesBrowserView(List<ICompletionProposal> proposals) {
		IWorkbenchWindow activeWindow = PlatformUI.getWorkbench().getActiveWorkbenchWindow();
		if (activeWindow == null || activeWindow.getActivePage() == null) {
			return;
		}
		IWorkbenchPage page = activeWindow.getActivePage();
		IViewReference[] references = page.getViewReferences();
		for (int i = 0; i < references.length; i++) {
			IViewReference viewReference = references[i];
			IViewPart view = viewReference.getView(false);
			if (view instanceof OverridesBrowser && page.isPartVisible(view) && textViewer != null) {
				List<ICompletionProposal> advancedCompletionProposals = ((OverridesBrowser)view)
						.getExtendCompletionProposals(textViewer.getDocument(), text, offset);
				if (advancedCompletionProposals.size() > 0) {
					proposals.addAll(0, advancedCompletionProposals);
				}
			}
		}
	}