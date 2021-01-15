	public int getIndex() {
		IJSONNode parent = getParentNode();
		if (parent == null)
			return -1; // error
		int index = 0;
		for (IJSONNode child = parent.getFirstChild(); child != null; child = child
				.getNextSibling()) {
			if (child == this)
				return index;
			index++;
		}
		return -1; // error
	}