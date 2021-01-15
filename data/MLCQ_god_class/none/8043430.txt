public class DefinitionFinder {

	private final StoredDefinitionFilter filter;

	public DefinitionFinder(final StoredDefinitionFilter filter) {
		this.filter = filter;
	}

	public List<Object> findDefinitions() {
		if (filter.getWorkspaceScope()) {
			return getDefinitionsOfWorkspace();
		} else {
			return getDefinitionsOfProject(filter.getCurrentProject());
		}
	}

	private List<Object> getDefinitionsOfWorkspace() {
		final List<Object> result = new ArrayList<Object>();
		for (IProject project : GlobalParser.getAllAnalyzedProjects()) {
			result.addAll(getDefinitionsOfProject(project));
		}
		return result;
	}

	private List<Object> getDefinitionsOfProject(final IProject project) {
		final List<Object> result = new ArrayList<Object>();
		ProjectSourceParser parser = GlobalParser.getProjectSourceParser(project);
		if (filter.showOnlyModules()) {
			result.addAll(parser.getModules());
		} else {
			for (Module module : parser.getModules()) {
				if (filter.filter(module)) {
					result.add(module);
				}
				for (Assignment ass : module.getAssignments()) {
					if (filter.filter(ass)) {
						result.add(ass);
					}
				}
			}
		}
		return result;
	}
}