	public HTMLContentBuilder(Document document) {
		super(document);
		Preferences prefs = HTMLCorePlugin.getDefault().getPluginPreferences();
		fTagCase = prefs.getInt(HTMLCorePreferenceNames.TAG_NAME_CASE);
		fAttrCase = prefs.getInt(HTMLCorePreferenceNames.ATTR_NAME_CASE);
		//	Element caseSettings = HTMLPreferenceManager.getHTMLInstance().getElement(PreferenceNames.PREFERRED_CASE);
		//	fTagCase = caseSettings.getAttribute(PreferenceNames.TAGNAME);
		//	fAttrCase = caseSettings.getAttribute(PreferenceNames.ATTRIBUTENAME);
	}