	public static void clear() {
		synchronized(RESOURCE_SET) {
			List<Resource> resources = RESOURCE_SET.getResources();
			for (Resource resource : resources) {
				resource.unload();
			}
		}
	}