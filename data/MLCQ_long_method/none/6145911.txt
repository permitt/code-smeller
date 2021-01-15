	public static IInclusionExclusionQuery getDefaultInclusionExclusionQuery(final Shell shell) {
		return new IInclusionExclusionQuery() {

			protected IPath[] fInclusionPattern;
			protected IPath[] fExclusionPattern;

			@Override
			public boolean doQuery(final BPListElement element, final boolean focusOnExcluded) {
				final boolean[] result= { false };
				Display.getDefault().syncExec(() -> {
					Shell sh = shell != null ? shell
							: DLTKUIPlugin.getActiveWorkbenchShell();
					ExclusionInclusionDialog dialog = new ExclusionInclusionDialog(
							sh, element, focusOnExcluded);
					result[0] = dialog.open() == Window.OK;
					fInclusionPattern = dialog.getInclusionPattern();
					fExclusionPattern = dialog.getExclusionPattern();
				});
				return result[0];
			}

			@Override
			public IPath[] getInclusionPattern() {
				return fInclusionPattern;
			}

			@Override
			public IPath[] getExclusionPattern() {
				return fExclusionPattern;
			}
		};
	}