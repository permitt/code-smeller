    @Override
	public String queryOverwrite(String pathString) {
        if (alwaysOverwrite) {
			return ALL;
		}

        final String returnCode[] = { CANCEL };
        final String msg = NLS.bind(ResourceNavigatorMessages.DropAdapter_overwriteQuery, pathString);
        final String[] options = { IDialogConstants.YES_LABEL,
                IDialogConstants.YES_TO_ALL_LABEL, IDialogConstants.NO_LABEL,
                IDialogConstants.CANCEL_LABEL };
        getDisplay().syncExec(() -> {
		    MessageDialog dialog = new MessageDialog(
		            getShell(),
					ResourceNavigatorMessages.DropAdapter_question, null, msg, MessageDialog.QUESTION, 0, options);
		    dialog.open();
		    int returnVal = dialog.getReturnCode();
		    String[] returnCodes = { YES, ALL, NO, CANCEL };
		    returnCode[0] = returnVal < 0 ? CANCEL : returnCodes[returnVal];
		});
        if (returnCode[0] == ALL) {
			alwaysOverwrite = true;
		}
        return returnCode[0];
    }