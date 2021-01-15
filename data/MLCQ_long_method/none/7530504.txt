	public S userFlag(String userFlag) {
		assertReceiver();
		this.receiver.setUserFlag(userFlag);
		return _this();
	}