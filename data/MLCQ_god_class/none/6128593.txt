public class PreferencesLookupDelegate implements IPreferencesLookupDelegate {

	private IPreferencesService service;
	private IScopeContext[] contexts;

	protected IScopeContext getTopScopeContext() {
		return contexts[0];
	}

	/**
	 * Creates a new delegate instance
	 *
	 * <p>
	 * A project may be specified to retrieve project specific value.
	 * </p>
	 *
	 * @param project
	 *            project reference, may be <code>null</code>
	 */
	public PreferencesLookupDelegate(IProject project) {
		this.service = Platform.getPreferencesService();
		this.contexts = getLookupScopes(project);
	}

	public PreferencesLookupDelegate(IScriptProject scriptProject) {
		this((scriptProject == null) ? null : scriptProject.getProject());
	}

	/**
	 * Returns a string preference value
	 *
	 * @param qualifier
	 *            preference key qualifier (plugin id)
	 * @param key
	 *            preference key
	 *
	 * @return preference value or an empty string if the preference is not
	 *         defined
	 */
	@Override
	public String getString(String qualifier, String key) {
		return service.getString(qualifier, key, "", contexts); //$NON-NLS-1$
	}

	/**
	 * Returns a int preference value
	 *
	 * @param qualifier
	 *            preference key qualifier (plugin id)
	 * @param key
	 *            preference key
	 *
	 * @return preference value or an empty string if the preference is not
	 *         defined
	 */
	@Override
	public int getInt(String qualifier, String key) {
		return service.getInt(qualifier, key, 0, contexts);
	}

	/**
	 * Returns a boolean preference value
	 *
	 * @param qualifier
	 *            preference key qualifier (plugin id)
	 * @param key
	 *            preference key
	 *
	 * @return preference value or <code>false</code> if the preference is not
	 *         defined
	 */
	@Override
	public boolean getBoolean(String qualifier, String key) {
		return service.getBoolean(qualifier, key, false, contexts);
	}

	private IScopeContext[] getLookupScopes(IProject project) {
		List<IScopeContext> list = new ArrayList<>(3);
		list.add(InstanceScope.INSTANCE);
		list.add(DefaultScope.INSTANCE);

		if (project != null) {
			list.add(0, new ProjectScope(project));
		}

		return list.toArray(new IScopeContext[list.size()]);
	}

}