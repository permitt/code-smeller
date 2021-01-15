	private class MainListener implements IMainLaunchConfigurationTabListener {
		@Override
		public void projectChanged(IProject project) {
			refreshInterpreters();
		}

		@Override
		public void interactiveChanged(boolean state) {
		}
	}