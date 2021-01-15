public abstract class SimpleValueProperty<S, T> extends ValueProperty<S, T> {
	@Override
	protected abstract T doGetValue(S source);

	@Override
	protected abstract void doSetValue(S source, T value);

	/**
	 * Returns a listener capable of adding or removing itself as a listener on
	 * a source object using the the source's "native" listener API. Events
	 * received from the source objects are parlayed to the specified listener
	 * argument.
	 * <p>
	 * This method returns null if the source object has no listener APIs for
	 * this property.
	 *
	 * @param listener
	 *            the property listener to receive events
	 * @return a native listener which parlays property change events to the
	 *         specified listener, or null if the source object has no listener
	 *         APIs for this property.
	 * @noreference This method is not intended to be referenced by clients.
	 */
	public abstract INativePropertyListener<S> adaptListener(
			ISimplePropertyListener<S, ValueDiff<? extends T>> listener);

	@Override
	public IObservableValue<T> observe(Realm realm, S source) {
		return new SimplePropertyObservableValue<>(realm, source, this);
	}

	@Override
	public <U extends S> IObservableList<T> observeDetail(IObservableList<U> master) {
		return new ListSimpleValueObservableList<>(master, this);
	}

	@Override
	public <U extends S> IObservableMap<U, T> observeDetail(IObservableSet<U> master) {
		return new SetSimpleValueObservableMap<>(master, this);
	}

	@Override
	public <K, V extends S> IObservableMap<K, T> observeDetail(IObservableMap<K, V> master) {
		return new MapSimpleValueObservableMap<>(master, this);
	}
}