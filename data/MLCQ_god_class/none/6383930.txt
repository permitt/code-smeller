public class MockEditorActionBarContributor extends EditorActionBarContributor {
    protected CallHistory callHistory;

    protected IEditorPart target;

    protected int ACTION_COUNT = 5;

    protected MockAction[] actions;

    /**
     * Constructor for MockEditorActionBarContributor
     */
    public MockEditorActionBarContributor() {
        super();
        callHistory = new CallHistory(this);
    }

    public CallHistory getCallHistory() {
        return callHistory;
    }

    /**
     * @see IEditorActionBarContributor#init(IActionBars)
     */
    @Override
	public void init(IActionBars bars) {
        callHistory.add("init");
        actions = new MockAction[ACTION_COUNT];
        for (int nX = 0; nX < ACTION_COUNT; nX++) {
            actions[nX] = new MockAction(Integer.toString(nX));
            if (nX % 2 > 0) {
				actions[nX].setEnabled(false);
			}
        }
        super.init(bars);
    }

    /**
     * @see EditorActionBarContributor#contributeToToolBar(IToolBarManager)
     */
    @Override
	public void contributeToToolBar(IToolBarManager toolBarManager) {
        for (MockAction action : actions) {
            toolBarManager.add(action);
        }
    }

    /**
     * @see IEditorActionBarContributor#setActiveEditor(IEditorPart)
     */
    @Override
	public void setActiveEditor(IEditorPart targetEditor) {
        callHistory.add("setActiveEditor");
        target = targetEditor;
    }

    /**
     * Returns the active editor.
     */
    public IEditorPart getActiveEditor() {
        return target;
    }

    /**
     * Returns the actions.
     */
    public MockAction[] getActions() {
        return actions;
    }

    /**
     * Set the enablement for all actions.
     */
    public void enableActions(boolean b) {
        for (int nX = 0; nX < ACTION_COUNT; nX++) {
            actions[nX].setEnabled(b);
        }
    }

}