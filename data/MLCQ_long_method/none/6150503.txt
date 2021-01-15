	public void addRename(IResource rename, RenameArguments arguments) {
		Assert.isNotNull(rename);
		Assert.isNotNull(arguments);
		if (fRename == null) {
			fRename = new ArrayList<>(2);
			fRenameArguments = new ArrayList<>(2);
		}
		fRename.add(rename);
		fRenameArguments.add(arguments);
		if (fIgnoreCount == 0) {
			IPath newPath = rename.getFullPath().removeLastSegments(1).append(arguments.getNewName());
			internalAdd(new MoveDescription(rename, newPath));
		}
	}