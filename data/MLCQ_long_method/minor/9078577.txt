	Iterable<? extends File> getDefaultClasspath() {
		// default classpath
		ArrayList<File> files = new ArrayList<>();
		String classProp = System.getProperty("java.class.path"); //$NON-NLS-1$
		if ((classProp == null) || (classProp.length() == 0)) {
			return null;
		} else {
			StringTokenizer tokenizer = new StringTokenizer(classProp, File.pathSeparator);
			String token;
			while (tokenizer.hasMoreTokens()) {
				token = tokenizer.nextToken();
				File file = new File(token);
				if (file.exists()) {
					files.add(file);
				}
			}
		}
		return files;
	}