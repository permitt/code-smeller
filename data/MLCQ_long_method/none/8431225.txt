    @Override
    protected void configureFormat(FixedWidthFormat format) {
        super.configureFormat(format);

        if (padding != null) {
            format.setPadding(padding);
        }
    }