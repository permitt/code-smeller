	private void notifyClients() {
		Object[] clients = listeners.getListeners();
		for (Object client : clients) {
			((VisibilityListener) client).onVisibilityOrActivationChange();
		}
	}