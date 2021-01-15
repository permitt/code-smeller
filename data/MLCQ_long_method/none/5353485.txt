	@Override
	public void stop(BundleContext context) throws Exception {
		instance = null;
		super.stop(context);
	}