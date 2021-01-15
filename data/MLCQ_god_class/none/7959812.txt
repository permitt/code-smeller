public class TestCaseEventDispatcher extends Observable implements Observer {

	/**
	 * Constructor
	 */
	public TestCaseEventDispatcher() {
		super();
	}

	/* (non-Javadoc)
	 * @see java.util.Observer#update(java.util.Observable, java.lang.Object)
	 */
	@Override
	public void update(final Observable observer, final Object event) {
		setChanged();
		notifyObservers(event);
		Display.getDefault().asyncExec(new Runnable() {
			@Override
			public void run() {
				Display.getCurrent().readAndDispatch();
			}
		});
	}
}