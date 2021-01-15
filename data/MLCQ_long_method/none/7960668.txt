	public TitanValue_Array(final TitanValue_Array<T> otherValue) {
		clazz = otherValue.clazz;
		array_size = otherValue.array_size;
		indexOffset = otherValue.indexOffset;
		array_elements = new Base_Type[array_size];

		for (int i = 0; i < array_size; ++i) {
			try {
				final T helper = clazz.newInstance();
				helper.operator_assign(otherValue.array_elements[i]);
				array_elements[i] = helper;
			} catch (InstantiationException e) {
				throw new TtcnError(MessageFormat.format("Internal error: class `{0}'' could not be instantiated ({1}).", clazz, e));
			} catch (IllegalAccessException e) {
				throw new TtcnError(MessageFormat.format("Internal error: class `{0}'' could not be instantiated ({1}).", clazz, e));
			}
		}
	}