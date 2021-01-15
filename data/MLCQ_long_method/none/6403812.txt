	boolean persist() {
		XMLMemento persistedState = (XMLMemento) getEditorState();
		if (persistedState == null)
			return false;

		StringWriter writer = new StringWriter();
		try {
			persistedState.save(writer);
			getModel().getPersistedState().put(MEMENTO_KEY, writer.toString());
		} catch (IOException e) {
			WorkbenchPlugin.log(e);
			return false;
		}

		return true;
	}