	@Override
	public void beginTask(String name, int totalWork) {
		monitor.beginTask(name, totalWork);
		fireMsgString(name);
	}