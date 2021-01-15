  public Image getImage()
  {
    XSDWildcard xsdWildcard = (XSDWildcard) target;
    
    if (xsdWildcard.eContainer() instanceof XSDParticle)
    {
      if (isReadOnly())
      {
        return XSDEditorPlugin.getPlugin().getIcon("obj16/XSDAnydis.gif"); //$NON-NLS-1$
      }
      return XSDEditorPlugin.getXSDImage("icons/XSDAny.gif"); //$NON-NLS-1$
    }
    else
    {
      if (isReadOnly())
      {
        return XSDEditorPlugin.getPlugin().getIcon("obj16/XSDAnyAttributedis.gif"); //$NON-NLS-1$
      }
      return XSDEditorPlugin.getXSDImage("icons/XSDAnyAttribute.gif"); //$NON-NLS-1$
    }
  }