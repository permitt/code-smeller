	public String getPassword() {
		final UsernamePassword userPass = getUserPass();
		final String pw = userPass.getPasswordAsString();
		userPass.resetPassword();
		return pw;
	}