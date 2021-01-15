public class FnLowerCase extends Function {
	private static Collection _expected_args = null;

	/**
	 * Constructor for FnLowerCase.
	 */
	public FnLowerCase() {
		super(new QName("lower-case"), 1);
	}

	/**
	 * Evaluate the arguments.
	 * 
	 * @param args
	 *            are evaluated.
	 * @throws DynamicError
	 *             Dynamic error.
	 * @return The evaluation of the arguments being converted to lower case.
	 */
	public ResultSequence evaluate(Collection args, org.eclipse.wst.xml.xpath2.api.EvaluationContext ec) throws DynamicError {
		return lower_case(args);
	}

	/**
	 * Convert arguments to lower case.
	 * 
	 * @param args
	 *            are converted to lower case.
	 * @throws DynamicError
	 *             Dynamic error.
	 * @return The result of converting the arguments to lower case.
	 */
	public static ResultSequence lower_case(Collection args)
			throws DynamicError {
		Collection cargs = Function.convert_arguments(args, expected_args());

		ResultSequence arg1 = (ResultSequence) cargs.iterator().next();

		if (arg1.empty()) {
			return new XSString("");
		}

		String str = ((XSString) arg1.first()).value();

		return new XSString(str.toLowerCase());
	}

	/**
	 * Calculate the expected arguments.
	 * 
	 * @return The expected arguments.
	 */
	public synchronized static Collection expected_args() {
		if (_expected_args == null) {
			_expected_args = new ArrayList();
			_expected_args.add(new SeqType(new XSString(), SeqType.OCC_QMARK));
		}

		return _expected_args;
	}
}