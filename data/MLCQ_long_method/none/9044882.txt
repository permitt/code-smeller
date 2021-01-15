public void testMethodWithInnerTypeInClassFile2() throws JavaModelException {
	IClassFile cf = getClassFile("Resolve", "zzz.jar", "", "MyClass2$Inner.class");
	IJavaElement[] elements = codeSelect(cf, "method", "method");
	assertElementsEqual(
		"Unexpected elements",
		"method(MyClass2.Inner[]) [in MyClass2 [in MyClass2.class [in <default> [in zzz.jar [in Resolve]]]]]",
		elements
	);

	IMethod method = (IMethod) elements[0];
	ISourceRange sourceRange = method.getSourceRange();
	String methodString = "void method(MyClass2.Inner[] arg){}";
	int o = cf.getSource().indexOf(methodString);
	int l = methodString.length();
	assertEquals("Unexpected offset", o, sourceRange.getOffset());
	assertEquals("Unexpected length", l, sourceRange.getLength());
}