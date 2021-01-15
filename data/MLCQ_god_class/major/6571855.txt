public abstract class WorkbenchPreferenceExtensionNode extends WorkbenchPreferenceExpressionNode 
    implements IComparableContribution {
	
  // RAP [fappel]: key to save page on the session to allow multiple sessions
  private static final String ID_PAGE
    = WorkbenchPreferenceExtensionNode.class.getName() + "#Page"; //$NON-NLS-1$
  
	private Collection keywordReferences;
	
	private IConfigurationElement configurationElement;

	private ImageDescriptor imageDescriptor;

	private Image image;

	private Collection keywordLabelCache;
	
	private int priority;

	private String pluginId;
	
	/**
	 * Create a new instance of the reciever.
	 * 
	 * @param id
	 * @param configurationElement 
	 */
	public WorkbenchPreferenceExtensionNode(String id, IConfigurationElement configurationElement) {
		super(id);
		this.configurationElement = configurationElement;
		this.pluginId = configurationElement.getNamespaceIdentifier();
	}

	/**
	 * Get the ids of the keywords the receiver is bound to.
	 * 
	 * @return Collection of <code>String</code>.  Never <code>null</code>.
	 */
	public Collection getKeywordReferences() {
		if (keywordReferences == null) {
			IConfigurationElement[] references = getConfigurationElement()
					.getChildren(IWorkbenchRegistryConstants.TAG_KEYWORD_REFERENCE);
			HashSet list = new HashSet(references.length);
			for (int i = 0; i < references.length; i++) {
				IConfigurationElement page = references[i];
				String id = page.getAttribute(IWorkbenchRegistryConstants.ATT_ID);
				if (id != null) {
					list.add(id);
				}
			}

			if (!list.isEmpty()) {
				keywordReferences = list;
			} else {
				keywordReferences = Collections.EMPTY_SET;
			}
			
		}
		return keywordReferences;
	}

	/**
	 * Get the labels of all of the keywords of the receiver.
	 * 
	 * @return Collection of <code>String</code>.  Never <code>null</code>.
	 */
	public Collection getKeywordLabels() {
		if (keywordLabelCache != null) {
			return keywordLabelCache;
		}
		
		Collection refs = getKeywordReferences();
		
		if(refs == Collections.EMPTY_SET) {
			keywordLabelCache = Collections.EMPTY_SET; 
			return keywordLabelCache;
		}
		
		keywordLabelCache = new ArrayList(refs.size());
		Iterator referenceIterator = refs.iterator();
		while(referenceIterator.hasNext()){
			Object label = KeywordRegistry.getInstance().getKeywordLabel(
					(String) referenceIterator.next());
			if(label != null) {
				keywordLabelCache.add(label);
			}
		}
		
		return keywordLabelCache;
	}
	
	/**
	 * Clear the keyword cache, if any.
	 */
	public void clearKeywords() {
		keywordLabelCache = null;
	}

	/* (non-Javadoc)
	 * @see org.eclipse.jface.preference.IPreferenceNode#disposeResources()
	 */
	public void disposeResources() {
        if (image != null) {
// RAP [fappel]: Resource disposal not available in RAP
//            image.dispose();
            image = null;
        }
        if( getPage() != null ) {
          getPage().dispose();
          removePage();
        }
        super.disposeResources();
	}

	/* (non-Javadoc)
	 * @see org.eclipse.jface.preference.IPreferenceNode#getLabelImage()
	 */
	public Image getLabelImage() {		
        if (image == null) {
        	ImageDescriptor desc = getImageDescriptor();
        	if (desc != null) {
				image = imageDescriptor.createImage();
			}
        }
        return image;
    }


	/* (non-Javadoc)
	 * @see org.eclipse.jface.preference.IPreferenceNode#getLabelText()
	 */
	public String getLabelText() {
		return getConfigurationElement().getAttribute(IWorkbenchRegistryConstants.ATT_NAME);
	}

    /**
     * Returns the image descriptor for this node.
     * 
     * @return the image descriptor
     */
    public ImageDescriptor getImageDescriptor() {
    	if (imageDescriptor != null) {
			return imageDescriptor;
		}
    	
    	String imageName = getConfigurationElement().getAttribute(IWorkbenchRegistryConstants.ATT_ICON);
		if (imageName != null) {
			String contributingPluginId = pluginId;
			imageDescriptor = AbstractUIPlugin.imageDescriptorFromPlugin(contributingPluginId, imageName);
		}
		return imageDescriptor;
    }
    
    /**
     * Return the configuration element.
     * 
     * @return the configuration element
     */
	public IConfigurationElement getConfigurationElement() {
		return configurationElement;
	}
	
	/* (non-Javadoc)
	 * @see org.eclipse.ui.activities.support.IPluginContribution#getLocalId()
	 */
	public String getLocalId() {
		return getId();
	}

	/* (non-Javadoc)
	 * @see org.eclipse.ui.activities.support.IPluginContribution#getPluginId()
	 */
	public String getPluginId() {
		return pluginId;
	}

    /* (non-Javadoc)
     * @see org.eclipse.ui.model.IComparableContribution#getAdapter(java.lang.Class)
     */
    public Object getAdapter(Class adapter)
    {
        if (adapter == IConfigurationElement.class)
            return getConfigurationElement();
        return null;
    }

    /* (non-Javadoc)
     * @see org.eclipse.ui.model.IComparableContribution#getLabel()
     */
    public String getLabel()
    {
        return getLabelText();
    }

    /* (non-Javadoc)
     * @see org.eclipse.ui.model.IComparableContribution#getPriority()
     */
    public int getPriority()
    {
        return priority;
    }

    public void setPriority(int pri)
    {
        priority = pri;
    }
    
    // RAP [fappel]: override to allow multiple sessions 
    public void setPage( final IPreferencePage newPage ) {
      RWT.getUISession().setAttribute( ID_PAGE + getId() , newPage );
    }
    
    // RAP [fappel]: override to allow multiple sessions 
    public IPreferencePage getPage() {
      return ( IPreferencePage )RWT.getUISession().getAttribute( ID_PAGE  + getId() );
    }
    
    // RAP [fappel]: allow to remove page from session store after disposal
    private void removePage() {
      RWT.getUISession().removeAttribute( ID_PAGE  + getId() );
    }

}