public final class DefineDataContentProvider implements IStructuredContentProvider {

	@Override
	public Object[] getElements(final Object inputElement) {
		if (inputElement != null) {
			if (inputElement instanceof DefineSectionHandler) {
				return ((DefineSectionHandler) inputElement).getDefinitions().toArray();
			}
		}

		return new Object[] {};
	}

	@Override
	public void dispose() {
		//Do nothing
	}

	@Override
	public void inputChanged(final Viewer viewer, final Object oldInput, final Object newInput) {
		//Do nothing
	}
}