public void testSuperTypeHierarchyWithMissingBinary() throws JavaModelException {
	IJavaProject project = getJavaProject("TypeHierarchy");
	IClasspathEntry[] originalClasspath = project.getRawClasspath();
	try {
		int length = originalClasspath.length;
		IClasspathEntry[] newClasspath = new IClasspathEntry[length+1];
		System.arraycopy(originalClasspath, 0, newClasspath, 0, length);
		newClasspath[length] = JavaCore.newLibraryEntry(new Path("/TypeHierarchy/test49809.jar"), null, null);
		project.setRawClasspath(newClasspath, null);
		ICompilationUnit cu = getCompilationUnit("/TypeHierarchy/src/q3/Z.java");
		IType type = cu.getType("Z");
		ITypeHierarchy hierarchy = type.newSupertypeHierarchy(null);
		assertHierarchyEquals(
				"Focus: Z [in Z.java [in q3 [in src [in TypeHierarchy]]]]\n" +
				"Super types:\n" +
				"  Y49809 [in Y49809.class [in p49809 [in test49809.jar [in TypeHierarchy]]]]\n" +
				"Sub types:\n",
			hierarchy
		);
	} finally {
		project.setRawClasspath(originalClasspath, null);
	}
}