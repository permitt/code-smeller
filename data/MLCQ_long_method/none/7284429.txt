    @Override
    public final void connect(Repository source, ProxyInfoProvider proxyInfoProvider) throws ConnectionException,
            AuthenticationException {
        connect(source, null, proxyInfoProvider);
    }