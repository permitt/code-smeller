	public HeaderPanel(String id, String appName) {
		super(id);
		setOutputMarkupPlaceholderTag(true);
		add(new Label("appName", Strings.isEmpty(appName) ? "&nbsp;" : appName).setEscapeModelStrings(false));
	}