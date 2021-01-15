	@Override
	public int match(MethodDeclaration node, MatchingNodeSet nodeSet) {
		// this locator matches only references
		return IMPOSSIBLE_MATCH;
	}