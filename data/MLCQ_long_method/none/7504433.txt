	@Override
	public Cursor<T> open() {
		this.delegate = delegate.open();
		return this;
	}