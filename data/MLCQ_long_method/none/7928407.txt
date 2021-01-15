	public void addPage(int pageIndex, IEditorPart editor, IEditorInput input)
			throws PartInitException {
		super.addPage(pageIndex,editor,input);
		if (editor instanceof DesignEditor) {
			bpmnDiagrams.add(pageIndex,((DesignEditor)editor).getBpmnDiagram());
			currentSelections.add(new PictogramElement[]{});
		}
	}