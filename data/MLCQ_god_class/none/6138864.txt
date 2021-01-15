public interface IElementHandler {

	/**
	 * Handler for element record
	 * 
	 * @param element
	 *            Element returned from database record
	 */
	public void handle(Element element);
}