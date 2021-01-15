	public void setForeground(Color fg) {
		super.setForeground(fg);
		titleRegion.setForeground(fg);
		if (messageRegion != null)
			messageRegion.setForeground(fg);
	}