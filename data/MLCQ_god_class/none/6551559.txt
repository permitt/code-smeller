public class ObservableMapCellLabelProvider extends CellLabelProvider {

	/**
	 * Observable maps typically mapping from viewer elements to label values.
	 * Subclasses may use these maps to provide custom labels.
	 * 
	 * @since 1.4
	 */
	protected IObservableMap[] attributeMaps;

	private IMapChangeListener mapChangeListener = new IMapChangeListener() {
		public void handleMapChange(MapChangeEvent event) {
			Set affectedElements = event.diff.getChangedKeys();
			LabelProviderChangedEvent newEvent = new LabelProviderChangedEvent(
					ObservableMapCellLabelProvider.this, affectedElements
							.toArray());
			fireLabelProviderChanged(newEvent);
		}
	};

	/**
	 * Creates a new label provider that tracks changes to one attribute.
	 * 
	 * @param attributeMap
	 */
	public ObservableMapCellLabelProvider(IObservableMap attributeMap) {
		this(new IObservableMap[] { attributeMap });
	}

	/**
	 * Creates a new label provider that tracks changes to more than one
	 * attribute. This constructor should be used by subclasses that override
	 * {@link #update(ViewerCell)} and make use of more than one attribute.
	 * 
	 * @param attributeMaps
	 */
	protected ObservableMapCellLabelProvider(IObservableMap[] attributeMaps) {
		System.arraycopy(attributeMaps, 0,
				this.attributeMaps = new IObservableMap[attributeMaps.length],
				0, attributeMaps.length);
		for (int i = 0; i < attributeMaps.length; i++) {
			attributeMaps[i].addMapChangeListener(mapChangeListener);
		}
	}

	public void dispose() {
		for (int i = 0; i < attributeMaps.length; i++) {
			attributeMaps[i].removeMapChangeListener(mapChangeListener);
		}
		super.dispose();
		this.attributeMaps = null;
		this.mapChangeListener = null;
	}

	public void update(ViewerCell cell) {
		Object element = cell.getElement();
		Object value = attributeMaps[0].get(element);
		cell.setText(value == null ? "" : value.toString()); //$NON-NLS-1$
	}

}