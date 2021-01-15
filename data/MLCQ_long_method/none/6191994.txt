	@Override
	public <T> T getAdapter(Class<T> adapter) {
		if (adapter.isInstance(this)) {
			return adapter.cast(this);
		} else if (Repository.class.equals(adapter)) {
			return adapter.cast(getRepository());
		}
		return null;
	}