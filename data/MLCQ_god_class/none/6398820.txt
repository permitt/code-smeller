	public static class ThemeRegistryModifiedHandler implements EventHandler {
		@Override
		public void handleEvent(org.osgi.service.event.Event event) {
			populateThemeRegistries(getThemeRegistry(), getFontRegistry(), getColorRegistry(),
					getTheme(), getColorsAndFontsTheme());
			sendThemeDefinitionChangedEvent();
		}

		protected org.eclipse.e4.ui.css.swt.theme.ITheme getTheme() {
			IThemeEngine themeEngine = getContext().get(IThemeEngine.class);
			return themeEngine != null ? themeEngine.getActiveTheme() : null;
		}

		protected ThemeRegistry getThemeRegistry() {
			return (ThemeRegistry) getContext().get(IThemeRegistry.class);
		}

		protected FontRegistry getFontRegistry() {
			return getColorsAndFontsTheme().getFontRegistry();
		}

		protected ColorRegistry getColorRegistry() {
			return getColorsAndFontsTheme().getColorRegistry();
		}

		protected ITheme getColorsAndFontsTheme() {
			return WorkbenchThemeManager.getInstance().getCurrentTheme();
		}

		private IEclipseContext getContext() {
			return WorkbenchThemeManager.getInstance().context;
		}

		protected void sendThemeDefinitionChangedEvent() {
			MApplication application = getContext().get(MApplication.class);
			getInstance().eventBroker.send(UIEvents.UILifeCycle.THEME_DEFINITION_CHANGED,
					application);
		}

		protected void populateThemeRegistries(ThemeRegistry themeRegistry,
				FontRegistry fontRegistry, ColorRegistry colorRegistry,
				org.eclipse.e4.ui.css.swt.theme.ITheme cssTheme, ITheme theme) {
			IPreferenceStore store = PrefUtil.getInternalPreferenceStore();
			for (FontDefinition definition : themeRegistry.getFonts()) {
				if (definition.isOverridden() || definition.isAddedByCss()) {
					populateDefinition(cssTheme, theme, fontRegistry, definition, store);
				}
			}
			for (ColorDefinition definition : themeRegistry.getColors()) {
				if (definition.isOverridden() || definition.isAddedByCss()) {
					populateDefinition(cssTheme, theme, colorRegistry, definition, store);
				}
			}
		}

		protected void populateDefinition(org.eclipse.e4.ui.css.swt.theme.ITheme cssTheme,
				ITheme theme, ColorRegistry registry, ColorDefinition definition,
				IPreferenceStore store) {
			ThemeElementHelper.populateDefinition(cssTheme, theme, registry, definition, store);
		}

		protected void populateDefinition(org.eclipse.e4.ui.css.swt.theme.ITheme cssTheme,
				ITheme theme, FontRegistry registry, FontDefinition definition,
				IPreferenceStore store) {
			ThemeElementHelper.populateDefinition(cssTheme, theme, registry, definition, store);
		}
	}