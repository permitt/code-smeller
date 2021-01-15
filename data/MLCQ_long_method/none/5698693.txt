	public PropertiesVocabSource(Properties prop) {
		assert (prop != null);
		this.prop = prop;
		vocabs = readVocab(prop);
	}