	private static void openOther(ExecutionEvent event, IWorkbenchWindow workbenchWindow, MApplication app,
			EPartService partService) {
		Shell shell = HandlerUtil.getActiveShell(event);
		IEclipseContext ctx = workbenchWindow.getService(IEclipseContext.class);
		EModelService modelService = workbenchWindow.getService(EModelService.class);
		MWindow window = workbenchWindow.getService(MWindow.class);

		final ShowViewDialog dialog = new ShowViewDialog(shell, app, window, modelService, partService, ctx);
		dialog.open();

		if (dialog.getReturnCode() == Window.CANCEL) {
			return;
		}

		final MPartDescriptor[] descriptors = dialog.getSelection();
		for (MPartDescriptor descriptor : descriptors) {
			openView(workbenchWindow, descriptor, partService);
		}
	}