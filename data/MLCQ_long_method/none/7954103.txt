	@Override
	/** {@inheritDoc} */
	public void setMyScope(final Scope scope) {
		super.setMyScope(scope);
		if (unnamedPart != null) {
			unnamedPart.setMyScope(scope);
		}
		if (namedPart != null) {
			namedPart.setMyScope(scope);
		}
	}