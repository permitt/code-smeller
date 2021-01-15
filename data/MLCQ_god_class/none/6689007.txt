public class XSLValidationMessage extends ValidationMessage
{
	private XSLNode node;
	private int realSeverity;

	/**
	 * Create a new instance of this.
	 * 
	 * @param message
	 *            The message for the validation message.
	 * @param lineNumber
	 *            The line location of the message.
	 * @param columnNumber
	 *            The column location of the message.
	 * @param uri
	 *            The uri of the file the message is for.
	 */
	public XSLValidationMessage(String message, int lineNumber, int columnNumber, String uri)
	{
		super(message, lineNumber, columnNumber, uri);
	}
	
	/**
	 * Set the node that this message applies to.
	 * 
	 * @param node the node
	 */
	public void setNode(XSLNode node)
	{
		this.node = node;
	}

	/**
	 * Get the node that this message applies to.
	 * @return the node
	 */
	public XSLNode getNode()
	{
		return node;
	}
	
	/**
	 * The severity set here should be the org.eclipse.wst.validation.internal.provisional.core.IMessage severity.
	 */
	@Override
	public void setSeverity(int sev)
	{
		this.realSeverity = sev;
		// the superclass only understands high and low.
		int severity;
		switch(sev)
		{
			case IMessage.HIGH_SEVERITY:
				severity = ValidationMessage.SEV_HIGH;
				break;
			default:
				severity = ValidationMessage.SEV_LOW;
		}
		super.setSeverity(severity);
	}
	
	/**
	 * Workaround for superclass's bizarre handling of severity
	 * 
	 * @return
	 */
	public int getRealSeverity()
	{
		return realSeverity;
	}
	
	@Override
	public String toString()
	{
		return node.toString();
	}
}