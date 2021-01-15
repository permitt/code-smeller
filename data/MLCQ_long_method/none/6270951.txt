	@Override
	protected void blockingFetch(Repository repo, ReplicaFetchRequest req)
			throws NotSupportedException, TransportException {
		try (Transport transport = Transport.open(repo, uri)) {
			RemoteConfig rc = getRemoteConfig();
			if (rc != null) {
				transport.applyConfig(rc);
			}
			fetch(transport, req);
		}
	}