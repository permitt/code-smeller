	@Override
	protected InternalExBacktrackingBug325745TestLanguageParser createParser(XtextTokenStream stream) {
		return new InternalExBacktrackingBug325745TestLanguageParser(stream, getGrammarAccess());
	}