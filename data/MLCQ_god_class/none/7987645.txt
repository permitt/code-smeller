public class EOR extends Token {

	/**
	 * Constructor
	 * @param token the token
	 */
	public EOR(final String token) {
		super(token);
	}

	@Override
	public int getType() {
		return Constants.END_OF_RECORD;
	}

}