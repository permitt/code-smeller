	public List<String> getVariables() {
		if (variables == null) {
			variables = new EDataTypeUniqueEList<String>(String.class, this, ApplicationPackageImpl.APPLICATION__VARIABLES);
		}
		return variables;
	}