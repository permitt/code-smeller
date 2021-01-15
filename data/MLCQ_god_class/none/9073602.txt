public abstract class SearchRequestor {

	/**
	 * Accepts the given search match.
	 *
	 * @param match the found match
	 * @throws CoreException
	 */
	public abstract void acceptSearchMatch(SearchMatch match) throws CoreException;

	/**
	 * Notification sent before starting the search action.
	 * Typically, this would tell a search requestor to clear previously
	 * recorded search results.
	 * <p>
	 * The default implementation of this method does nothing. Subclasses
	 * may override.
	 * </p>
	 */
	public void beginReporting() {
		// do nothing
	}

	/**
	 * Notification sent after having completed the search action.
	 * Typically, this would tell a search requestor collector that no more
	 * results will be forthcoming in this search.
	 * <p>
	 * The default implementation of this method does nothing. Subclasses
	 * may override.
	 * </p>
	 */
	public void endReporting() {
		// do nothing
	}

	/**
	 * Intermediate notification sent when the given participant starts to
	 * contribute.
	 * <p>
	 * The default implementation of this method does nothing. Subclasses
	 * may override.
	 * </p>
	 *
	 * @param participant the participant that is starting to contribute
	 */
	public void enterParticipant(SearchParticipant participant) {
		// do nothing
	}

	/**
	 * Intermediate notification sent when the given participant is finished
	 * contributing.
	 * <p>
	 * The default implementation of this method does nothing. Subclasses
	 * may override.
	 * </p>
	 *
	 * @param participant the participant that finished contributing
	 */
	public void exitParticipant(SearchParticipant participant) {
		// do nothing
	}
}