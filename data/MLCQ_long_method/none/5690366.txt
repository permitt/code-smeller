        public BundleConfigurationProvider(String filename, Bundle bundle, BundleContext bundleContext) {
            super(filename, false);
            this.bundle = bundle;
            this.bundleContext = bundleContext;
        }