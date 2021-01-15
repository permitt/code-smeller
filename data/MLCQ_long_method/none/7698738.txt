	boolean testnext(int c) {
		if (t.token == c) {
			next();
			return true;
		} else
			return false;
	}