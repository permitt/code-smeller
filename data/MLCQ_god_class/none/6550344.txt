public abstract class AbstractIntegerListener extends AbstractPropertyListener {

    private IDynamicPropertyMap map;
    private int defaultValue;
    private String propertyId;
    
    public AbstractIntegerListener() {
    }
    
    public void attach(IDynamicPropertyMap map, String propertyId, int defaultValue) {
        this.defaultValue = defaultValue;
        this.propertyId = propertyId;
        if (this.map != null) {
            this.map.removeListener(this);
        }
        
        this.map = map;
        
        if (this.map != null) {
            this.map.addListener(new String[]{propertyId}, this);
        }
    }

    /* (non-Javadoc)
     * @see org.eclipse.ui.internal.preferences.AbstractPropertyListener#update()
     */
    protected void update() {
        handleValue(PropertyUtil.get(map, propertyId, defaultValue));
    }

    /**
     * @param b
     */
    protected abstract void handleValue(int b);
   
    
}