	public static final char[] extract(char[] str, int start, int length) {
		if (start == 0 && length == str.length)
			return str;

		char[] copy = new char[length];
		System.arraycopy(str, start, copy, 0, length);
		return copy;
	}