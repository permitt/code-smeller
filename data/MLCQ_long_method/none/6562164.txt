    public IEditorMatchingStrategy getEditorMatchingStrategy() {
        if (matchingStrategy == null && !matchingStrategyChecked) {
            matchingStrategyChecked = true;
            // RAP [bm]: Program
//            if (program == null && configurationElement != null) {
            if (configurationElement != null) {
            // RAPEND: [bm] 
                if (configurationElement.getAttribute(IWorkbenchRegistryConstants.ATT_MATCHING_STRATEGY) != null) {
                    try {
                        matchingStrategy = (IEditorMatchingStrategy) WorkbenchPlugin.createExtension(configurationElement, IWorkbenchRegistryConstants.ATT_MATCHING_STRATEGY);
                    } catch (CoreException e) {
                        WorkbenchPlugin.log("Error creating editor management policy for editor id " + getId(), e); //$NON-NLS-1$
                    }
                }
            }
        }
        return matchingStrategy;
    }