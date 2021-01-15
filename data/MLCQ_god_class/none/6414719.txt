public class UnionSetProperty<S, E> extends SetProperty<S, E> {
	private final ISetProperty<S, E>[] properties;
	private final Object elementType;

	/**
	 * @param properties
	 */
	public UnionSetProperty(ISetProperty<S, E>[] properties) {
		this(properties, null);
	}

	/**
	 * @param properties
	 * @param elementType
	 */
	public UnionSetProperty(ISetProperty<S, E>[] properties, Object elementType) {
		this.properties = properties;
		this.elementType = elementType;
	}

	@Override
	public Object getElementType() {
		return elementType;
	}

	@Override
	protected Set<E> doGetSet(S source) {
		Set<E> set = new HashSet<>();
		for (ISetProperty<S, E> property : properties)
			set.addAll(property.getSet(source));
		return set;
	}

	@Override
	protected void doSetSet(S source, Set<E> set) {
		throw new UnsupportedOperationException("UnionSetProperty is unmodifiable"); //$NON-NLS-1$
	}

	@Override
	protected void doUpdateSet(S source, SetDiff<E> diff) {
		throw new UnsupportedOperationException("UnionSetProperty is unmodifiable"); //$NON-NLS-1$
	}

	@Override
	public IObservableSet<E> observe(Realm realm, S source) {
		Set<IObservableSet<? extends E>> sets = new HashSet<IObservableSet<? extends E>>(properties.length);
		for (ISetProperty<S, E> property : properties) {
			sets.add(property.observe(realm, source));
		}
		IObservableSet<E> unionSet = new UnionSet<>(sets, elementType);

		for (IObservableSet<? extends E> set : sets) {
			PropertyObservableUtil.cascadeDispose(unionSet, set);
		}

		return unionSet;
	}
}