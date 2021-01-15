final class HedA extends HedInlineContainer {

	/**
	 */
	public HedA(ElementCollection collection) {
		super(HTML40Namespace.ElementName.A, collection);
		// CORRECT_EMPTY - GROUP_COMPACT
		correctionType = CORRECT_EMPTY;
	}

	/**
	 * %attrs;
	 */
	protected void createAttributeDeclarations() {
		if (attributes != null)
			return; // already created.
		if (attributeCollection == null)
			return; // fatal

		attributes = new CMNamedNodeMapImpl();

		// %attrs;
		attributeCollection.getAttrs(attributes);

		//different sets of attributes for html 4 & 5
		attributeCollection.createAttributeDeclarations(HTML40Namespace.ElementName.A, attributes);
	
	}

	/**
	 * Exclusion.
	 * <code>A</code> has the exclusion.
	 * It is <code>A</code> itself.
	 */
	public CMContent getExclusion() {
		if (exclusion != null)
			return exclusion; // already created.
		if (elementCollection == null)
			return null;

		exclusion = new CMGroupImpl(CMGroup.CHOICE, 1, 1);
		CMNode a = elementCollection.getNamedItem(HTML40Namespace.ElementName.A);
		if (a != null)
			exclusion.appendChild(a);

		return exclusion;
	}

	/**
	 */
	public CMNamedNodeMap getProhibitedAncestors() {
		if (prohibitedAncestors != null)
			return prohibitedAncestors;

		String[] names = {HTML40Namespace.ElementName.A, HTML40Namespace.ElementName.BUTTON};
		prohibitedAncestors = elementCollection.getDeclarations(names);

		return prohibitedAncestors;
	}
}