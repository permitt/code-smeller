	public String newlineWithIndent(int indent) {
		StringBuilder buf = new StringBuilder();
		addNewlineWithIndent(indent, buf);
		return buf.toString();
	}