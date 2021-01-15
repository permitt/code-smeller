	@Override
	/** {@inheritDoc} */
	public void findReferences(final ReferenceFinder referenceFinder, final List<Hit> foundIdentifiers) {
		if (parsedParameters != null) {
			parsedParameters.findReferences(referenceFinder, foundIdentifiers);
		}
	}