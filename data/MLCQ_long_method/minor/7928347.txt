	@Override
	public boolean select(Viewer viewer, Object parentElement, Object element) {
		IResource resource = null;
		if (element instanceof IFile) {
			resource = (IFile) element;
		}
		else
			return true;
		if (resource != null) {
			String name = resource.getName();
			for (int i = 0; i < patterns.length; i++) {
				if (name.endsWith(patterns[i]))
					return true;
			}
			return false;
		}
		return true;
	}