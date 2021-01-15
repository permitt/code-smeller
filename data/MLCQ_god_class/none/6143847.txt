public class Messages extends NLS {
	private static final String BUNDLE_NAME = "org.eclipse.dltk.internal.mylyn.search.messages"; //$NON-NLS-1$

	static {
		// load message values from bundle file
		reloadMessages();
	}

	public static void reloadMessages() {
		NLS.initializeMessages(BUNDLE_NAME, Messages.class);
	}

	public static String AbstractJavaRelationProvider_could_not_run_Java_search;

	public static String AbstractJavaRelationProvider_Mylyn_degree_of_separation;
}