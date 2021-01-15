@Deprecated
@SuppressWarnings("all")
public final class NotHandledException extends CommandException {

    /**
     * Generated serial version UID for this class.
     *
     * @since 3.1
     */
    private static final long serialVersionUID = 3256446914827726904L;

    /**
     * Creates a new instance of this class with the specified detail message.
     *
     * @param s
     *            the detail message.
     */
	@Deprecated
    public NotHandledException(String s) {
        super(s);
    }

    /**
     * Constructs a legacy <code>NotHandledException</code> based on the new
     * <code>NotHandledException</code>
     *
     * @param e
     *            The exception from which this exception should be created;
     *            must not be <code>null</code>.
     * @since 3.1
     */
	@Deprecated
    public NotHandledException(final org.eclipse.core.commands.NotHandledException e) {
        super(e.getMessage(), e);
    }
}