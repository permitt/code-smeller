public final class ExtensionAdditions extends ASTNode {

	private final List<ExtensionAddition> extensionAdditions;

	public ExtensionAdditions() {
		extensionAdditions = new ArrayList<ExtensionAddition>();
	}

	public ExtensionAdditions(final List<ExtensionAddition> extensionAdditions) {
		this.extensionAdditions = extensionAdditions;
		for (final ExtensionAddition extensionAddition : extensionAdditions) {
			extensionAddition.setFullNameParent(this);
		}
	}

	public void addExtensionAddition(final ExtensionAddition extensionAddition) {
		if (null != extensionAddition) {
			extensionAdditions.add(extensionAddition);
			extensionAddition.setFullNameParent(this);
		}
	}

	@Override
	/** {@inheritDoc} */
	public void setMyScope(final Scope scope) {
		super.setMyScope(scope);
		for (final ExtensionAddition extensionAddition : extensionAdditions) {
			extensionAddition.setMyScope(scope);
		}
	}

	public int getNofComps() {
		int result = 0;
		for (final ExtensionAddition extensionAddition : extensionAdditions) {
			result += extensionAddition.getNofComps();
		}
		return result;
	}

	public CompField getCompByIndex(final int index) {
		int offset = index;
		for (int i = 0; i < extensionAdditions.size(); i++) {
			final int subSize = extensionAdditions.get(i).getNofComps();

			if (offset < subSize) {
				return extensionAdditions.get(i).getCompByIndex(offset);
			}

			offset -= subSize;
		}

		// FATAL ERROR
		return null;
	}

	public boolean hasCompWithName(final Identifier identifier) {
		for (final ExtensionAddition extensionAddition : extensionAdditions) {
			if (extensionAddition.hasCompWithName(identifier)) {
				return true;
			}
		}

		return false;
	}

	public CompField getCompByName(final Identifier identifier) {
		for (final ExtensionAddition extensionAddition : extensionAdditions) {
			if (extensionAddition.hasCompWithName(identifier)) {
				return extensionAddition.getCompByName(identifier);
			}
		}

		// FATAL ERROR
		return null;
	}

	public void trCompsof(final CompilationTimeStamp timestamp, final IReferenceChain referenceChain, final boolean isSet) {
		for (final ExtensionAddition extensionAddition : extensionAdditions) {
			extensionAddition.trCompsof(timestamp, referenceChain, isSet);
		}
	}

	@Override
	/** {@inheritDoc} */
	public void findReferences(final ReferenceFinder referenceFinder, final List<Hit> foundIdentifiers) {
		if (extensionAdditions == null) {
			return;
		}

		for (final ExtensionAddition ea : extensionAdditions) {
			ea.findReferences(referenceFinder, foundIdentifiers);
		}
	}

	@Override
	/** {@inheritDoc} */
	protected boolean memberAccept(final ASTVisitor v) {
		if (extensionAdditions != null) {
			for (final ExtensionAddition ea : extensionAdditions) {
				if (!ea.accept(v)) {
					return false;
				}
			}
		}
		return true;
	}
}