	@Override
	public ModuleDeclaration parse(PossibleMatch possibleMatch) {
		ModuleDeclaration module = SourceParserUtil.getModuleDeclaration(
				(org.eclipse.dltk.core.ISourceModule) possibleMatch
						.getModelElement(), null);
		return module;
	}