	protected void notifyStateChanged(StateMachineContext<S, E> context) {
		if (log.isTraceEnabled()) {
			log.trace("Notify notifyStateChanged " + context);
		}
		ensembleListener.stateChanged(context);
	}