	public void test087() {
		DefaultCodeFormatterOptions preferences = new DefaultCodeFormatterOptions(DefaultCodeFormatterConstants.getEclipse21Settings());
		preferences.tab_char = DefaultCodeFormatterOptions.TAB;
		preferences.keep_simple_if_on_one_line = true;
		DefaultCodeFormatter codeFormatter = new DefaultCodeFormatter(preferences);
		runTest(codeFormatter, "test087", "A.java", CodeFormatter.K_STATEMENTS);//$NON-NLS-1$ //$NON-NLS-2$
	}