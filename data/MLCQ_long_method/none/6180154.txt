	private SWTBotStyledText getNonAncestorEditor(int index) {
		List<StyledText> texts = editor.bot().getFinder()
				.findControls(widgetOfType(StyledText.class));
		if (texts.size() == 2)
			return new SWTBotStyledText(texts.get(index));
		else if (texts.size() == 3)
			return new SWTBotStyledText(texts.get(index + 1));
		else
			throw new IllegalStateException(
					"Expected compare editor to contain 2 or 3 styled text widgets, but was "
							+ texts.size());
	}