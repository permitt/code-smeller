public void testBug346002() throws Exception {
	ClasspathContainerInitializer initializer = JavaCore.getClasspathContainerInitializer(JavaCore.USER_LIBRARY_CONTAINER_ID);
	String libraryName = "TEST";
	IPath containerPath = new Path(JavaCore.USER_LIBRARY_CONTAINER_ID);
	UserLibraryClasspathContainer containerSuggestion = new UserLibraryClasspathContainer(libraryName);
	initializer.requestClasspathContainerUpdate(containerPath.append(libraryName), null, containerSuggestion);

	String libPath = "C:/test/test.jar";

	IEclipsePreferences preferences = InstanceScope.INSTANCE.getNode(JavaCore.PLUGIN_ID);
	String propertyName = JavaModelManager.CP_USERLIBRARY_PREFERENCES_PREFIX+ "TEST";

	StringBuffer propertyValue = new StringBuffer(
			"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<userlibrary systemlibrary=\"false\" version=\"2\">\r\n<archive");
	propertyValue.append(" path=\"" + libPath + "\"/>\r\n");
	propertyValue.append("</userlibrary>\r\n");
	preferences.put(propertyName, propertyValue.toString());

	propertyName = JavaModelManager.CP_USERLIBRARY_PREFERENCES_PREFIX + "INVALID";
	propertyValue = new StringBuffer(
			"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<userlibrary systemlibrary=\"false\" version=\"2\">\r\n<archive");
	propertyValue.append(" path=\"\"/>");
	propertyValue.append("</userlibrary>\r\n");
	preferences.put(propertyName, propertyValue.toString());
	preferences.flush();

	try {
		simulateExitRestart();

		UserLibrary userLibrary = JavaModelManager.getUserLibraryManager().getUserLibrary(libraryName);
		assertNotNull(userLibrary);
		IPath entryPath = userLibrary.getEntries()[0].getPath();
		assertEquals("Path should be absolute", true, entryPath.isAbsolute());

		userLibrary = JavaModelManager.getUserLibraryManager().getUserLibrary("INVALID");
		assertNull(userLibrary);
	}
	catch (ClasspathEntry.AssertionFailedException e) {
		fail("Should not throw AssertionFailedException");
	}
}