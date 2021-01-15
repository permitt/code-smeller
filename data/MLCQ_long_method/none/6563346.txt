    Collection readRegistry(IExtensionRegistry in) {
        values.clear();
        ids.clear();
        // RAP [bm]: 
//        readRegistry(in, PlatformUI.PLUGIN_ID,
//                IWorkbenchRegistryConstants.PL_DECORATORS);
      readRegistry(in, PlatformUI.PLUGIN_EXTENSION_NAME_SPACE,
				IWorkbenchRegistryConstants.PL_DECORATORS);
        // RAPEND: [bm] 
        return values;
    }