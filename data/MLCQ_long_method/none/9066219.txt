public void testBug128877b() throws CoreException {
	IType type = getPackageFragment("JavaSearchBugs", "lib/b128877.jar", "pack").getOrdinaryClassFile("Test.class").getType();
	IMethod method = type.getMethod("Test", new String[] { "Ljava.lang.String;" });
	search(method, REFERENCES);
	assertSearchResults(
		"lib/b128877.jar pack.X$Sub(pack.X, java.lang.String) EXACT_MATCH"
	);
}