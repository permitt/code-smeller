	static boolean isPronoun (Markable m) {
		if (m.getContent() instanceof BaseToken) {
			BaseToken t = (BaseToken) m.getContent();
			if (t.getPartOfSpeech().startsWith("PRP")) // TODO: since only 3rd person pronouns are added as markables, no need to check
				return true;
		}
		return false;
	}