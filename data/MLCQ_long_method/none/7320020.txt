        public CLCHTTPProxyConfiguration(
            final String host,
            final int port,
            final String username,
            final String password) {
            Check.notNull(host, "host"); //$NON-NLS-1$

            this.host = host;
            this.port = port;
            this.username = username;
            this.password = password;
        }