        @Override
        protected void uninstallListeners(JComponent scrollPane) {
            super.uninstallListeners(scrollPane);
            scrollPane.removePropertyChangeListener(propertyChangeHandler);
        }