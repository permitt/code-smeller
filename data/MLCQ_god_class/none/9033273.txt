@SuppressWarnings({"rawtypes"})
public class JavaSearchGenericConstructorExactTests extends JavaSearchGenericConstructorTests {

	/**
	 * @param name
	 */
	public JavaSearchGenericConstructorExactTests(String name) {
		super(name, EXACT_RULE);
	}

	public static Test suite() {
		TestSuite suite = new Suite(JavaSearchGenericConstructorExactTests.class.getName());
		List tests = buildTestsList(JavaSearchGenericConstructorExactTests.class, 1, 0/* do not sort*/);
		for (int index=0, size=tests.size(); index<size; index++) {
			suite.addTest((Test)tests.get(index));
		}
		return suite;
	}

	/*
	 * Do not add line if this is not an exact match rule.
	 */
	void addResultLine(StringBuffer buffer, char[] line) {
		if (CharOperation.match(RESULT_EXACT_MATCH, line, true)) {
			super.addResultLine(buffer, line);
		}
	}

	/* (non-Javadoc)
	 * @see org.eclipse.jdt.core.tests.model.JavaSearchGenericTypeTests#removeFirstTypeArgument(char[])
	 */
	long removeFirstTypeArgument(char[] line) {
		return -1;
	}
}