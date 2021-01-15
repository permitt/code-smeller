	public boolean equals(Object other) {
		if (!(other instanceof ThrowsPattern)) {
			return false;
		}
		ThrowsPattern o = (ThrowsPattern) other;
		boolean ret = o.required.equals(this.required) && o.forbidden.equals(this.forbidden);
		return ret;
	}