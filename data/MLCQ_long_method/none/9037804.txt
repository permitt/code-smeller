public void test0001() throws JavaModelException {
	this.workingCopies = new ICompilationUnit[2];
	this.workingCopies[0] = getWorkingCopy(
		"/Completion/src/test/Test.java",
		"package test;"+
		"public class Test {\n" +
		"  void foo() {\n" +
 		"    MissingType<Object> m = null;\n" +
 		"    m.b\n" +
		"  }\n" +
		"}\n");

	this.workingCopies[1] = getWorkingCopy(
		"/Completion/src/missing/MissingType.java",
		"package missing;"+
		"public class MissingType<T> {\n" +
		"  public void bar() {};\n" +
		"}\n");

	CompletionTestsRequestor2 requestor = new CompletionTestsRequestor2(true, false, true, false, true);
	requestor.allowAllRequiredProposals();
	String str = this.workingCopies[0].getSource();
	String completeBehind = "m.b";
	int cursorLocation = str.lastIndexOf(completeBehind) + completeBehind.length();
	this.workingCopies[0].codeComplete(cursorLocation, requestor, this.wcOwner);

	int relevance1 = R_DEFAULT + R_RESOLVED + R_INTERESTING + R_CASE + R_NON_STATIC + R_NON_RESTRICTED + R_NO_PROBLEMS;
	int start1 = str.lastIndexOf("m.b") + "m.".length();
	int end1 = start1 + "b".length();
	int start2 = str.lastIndexOf("MissingType");
	int end2 = start2 + "MissingType".length();
	assertResults(
			"bar[METHOD_REF]{bar(), Lmissing.MissingType<Ljava.lang.Object;>;, ()V, bar, null, ["+start1+", "+end1+"], " + (relevance1) + "}\n" +
			"   MissingType[TYPE_REF]{missing.MissingType, missing, Lmissing.MissingType;, null, null, ["+start2+", "+end2+"], " + (relevance1) + "}",
			requestor.getResults());
}