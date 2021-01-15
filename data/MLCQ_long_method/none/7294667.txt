	private boolean isGrailsLaunch(ILaunchConfiguration launchConfiguration) {
		try {
			ILaunchConfigurationType type = launchConfiguration.getType();
			return GrailsCoreActivator.PLUGIN_ID.equals(type.getPluginIdentifier());
		} catch (CoreException ex) {
			return false;
		}
	}