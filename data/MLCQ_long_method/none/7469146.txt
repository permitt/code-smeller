	public NamedMongoScript(String name, String rawScript) {
		this(name, new ExecutableMongoScript(rawScript));
	}