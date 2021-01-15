	public boolean hasAnyScope(String... scopes) {
		boolean result = OAuth2ExpressionUtils.hasAnyScope(authentication, scopes);
		if (!result) {
			missingScopes.addAll(Arrays.asList(scopes));
		}
		return result;
	}