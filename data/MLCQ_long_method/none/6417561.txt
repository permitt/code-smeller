    private IFileEditorMapping[] getInput() {
        //Filter the mappings to be just those with a wildcard extension
        if (currentInput == null) {
            List wildcardEditors = new ArrayList();
            IFileEditorMapping[] allMappings = ((EditorRegistry)PlatformUI.getWorkbench()
                    .getEditorRegistry()).getUnifiedMappings();
            for (IFileEditorMapping allMapping : allMappings) {
                if (allMapping.getName().equals("*")) { //$NON-NLS-1$
					wildcardEditors.add(allMapping);
				}
            }
            currentInput = new IFileEditorMapping[wildcardEditors.size()];
            wildcardEditors.toArray(currentInput);
        }
        return currentInput;
    }