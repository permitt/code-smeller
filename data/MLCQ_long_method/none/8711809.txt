	@Override
	public void beginSession() {
		getPaintSurface().setStatusMessage(PaintExample.getResourceString(
			"session.Text.message"));
	}