	public String getTextValue() {
		ExtendedPropertiesAdapter adapter = ExtendedPropertiesAdapter.adapt(object);
		if (adapter!=null) {
			return adapter.getFeatureDescriptor(feature).getTextValue();
		}
		return getValue().toString();
	}