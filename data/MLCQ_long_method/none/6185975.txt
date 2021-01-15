	@Override
	public void execute(IProgressMonitor monitor) throws CoreException {
		String branchName = repository.getConfig().getFeatureBranchName(featureName);

		boolean dontCloseProjects = false;
		Repository gitRepo = repository.getRepository();
		BranchOperation branchOperation = new BranchOperation(
				gitRepo, branchName, dontCloseProjects);
		branchOperation.execute(monitor);
		result = branchOperation.getResult(gitRepo);
	}