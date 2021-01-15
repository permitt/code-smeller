    protected Color getHandleColor(IConfigRegistry configRegistry) {
        if (configRegistry != null) {
            Color color = configRegistry.getConfigAttribute(
                    FillHandleConfigAttributes.FILL_HANDLE_COLOR,
                    DisplayMode.NORMAL);

            if (color != null) {
                return color;
            }
        }
        return GUIHelper.getColor(0, 125, 10);
    }