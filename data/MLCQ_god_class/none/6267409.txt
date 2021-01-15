public class JGitHostConfigEntry extends HostConfigEntry {

	private Map<String, List<String>> multiValuedOptions;

	@Override
	public String getProperty(String name, String defaultValue) {
		// Upstream bug fix (SSHD-867): if there are _no_ properties at all, the
		// super implementation returns always null even if a default value is
		// given.
		//
		// See https://issues.apache.org/jira/projects/SSHD/issues/SSHD-867
		//
		// TODO: remove this override once we're based on sshd > 2.1.0
		Map<String, String> properties = getProperties();
		if (properties == null || properties.isEmpty()) {
			return defaultValue;
		}
		return super.getProperty(name, defaultValue);
	}

	/**
	 * Sets the multi-valued options.
	 *
	 * @param options
	 *            to set, may be {@code null} to set an empty map
	 */
	public void setMultiValuedOptions(Map<String, List<String>> options) {
		multiValuedOptions = options;
	}

	/**
	 * Retrieves all multi-valued options.
	 *
	 * @return an unmodifiable map
	 */
	@NonNull
	public Map<String, List<String>> getMultiValuedOptions() {
		Map<String, List<String>> options = multiValuedOptions;
		if (options == null) {
			return Collections.emptyMap();
		}
		return Collections.unmodifiableMap(options);
	}

}