	protected void addRepository(RemoteRepository repository) {
		if (this.repositories.contains(repository)) {
			return;
		}
		repository = getPossibleMirror(repository);
		repository = applyProxy(repository);
		repository = applyAuthentication(repository);
		this.repositories.add(0, repository);
	}