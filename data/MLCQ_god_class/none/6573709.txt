public interface IViewReference extends IWorkbenchPartReference {

    /**
     * Returns the secondary ID for the view.
     * 
     * @return the secondary ID, or <code>null</code> if there is no secondary id
     * @see IWorkbenchPage#showView(String, String, int)
     */
    public String getSecondaryId();

    /**
     * Returns the <code>IViewPart</code> referenced by this object.
     * Returns <code>null</code> if the view was not instantiated or
     * it failed to be restored.  Tries to restore the view
     * if <code>restore</code> is true.
     */
    public IViewPart getView(boolean restore);

    /**
     * Returns true if the view is a fast view otherwise returns false.
     * @since 1.1
     */
    public boolean isFastView();
}