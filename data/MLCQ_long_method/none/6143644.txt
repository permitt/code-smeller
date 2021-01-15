	protected String getDefaultProfileID() {
		StringBuffer buffer = new StringBuffer();
		String lang = getLanguage();
		if (lang != null && lang.length() > 0) {
			buffer.append("org.eclipse.dltk."); //$NON-NLS-1$
			buffer.append(lang.toLowerCase());
		} else {
			buffer.append(getClass().getName());
		}

		buffer.append(".formatter.profiles.default"); //$NON-NLS-1$
		return buffer.toString();
	}