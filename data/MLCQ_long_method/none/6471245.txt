	public JavaVMOption(String optionString, ImagePointer extraInfo) {
		if (optionString == null) {
			throw new IllegalArgumentException();
		}
		_optionString = optionString;
		_extraInfo = extraInfo;
	}