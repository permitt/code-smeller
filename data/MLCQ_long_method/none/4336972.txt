	public PersistentService getServiceType(Object serviceModule) {
		TopService ts = findTopService(serviceModule);

		if (ts == null)
			return null;

		return ts.getServiceType();
	}