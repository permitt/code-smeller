	public void testGetAutoEditStrategies() {

		// probably no display
		if (!fDisplayExists)
			return;

		IAutoEditStrategy[] strategies = fConfig.getAutoEditStrategies(fViewer, IDTDPartitions.DTD_DEFAULT);
		assertNotNull(strategies);
		assertTrue("there are no auto edit strategies", strategies.length > 0);
	}