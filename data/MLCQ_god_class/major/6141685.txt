public class ProjectSetup extends AbstractProjectSetup {

	public static class Option {
		Option() {
		}

		/**
		 * Performs the full build of the project.
		 */
		public static final Option BUILD = new NamedOption("BUILD");

		/**
		 * Disables the indexer before and enables it back after.
		 */
		public static final Option INDEXER_DISABLED = new NamedOption(
				"INDEXER_DISABLED");

		/**
		 * Waits for the indexer to complete after the project creation.
		 */
		public static final Option WAIT_INDEXES_READY = new NamedOption(
				"WAIT_INDEXES_READY");

		/**
		 * Enables some logging, makes sense only while debugging
		 */
		public static final Option VERBOSE = new NamedOption("VERBOSE");

		/**
		 * Specifies if project should be left closed after creation.
		 */
		public static final Option CLOSED = new NamedOption("CLOSED");

		/**
		 * Specifies the exclusion path, those files will be excluded during
		 * initial project creation, but can be created individually later.
		 *
		 * @see #createFile(String, Option)
		 */
		public static Option exclude(String path) {
			return new ExcludeOption(path);
		}
	}

	private static class NamedOption extends Option {
		private final String name;

		public NamedOption(String name) {
			this.name = name;
		}

		@Override
		public String toString() {
			return name;
		}
	}

	private static class ExcludeOption extends Option {
		final String path;

		public ExcludeOption(String path) {
			this.path = path;
		}
	}

	/**
	 * This method implements workaround when using this class in JUnit before
	 * 4.9 (without &#64;ClassRule) and should be called from the method
	 * annotated with &#64;BeforeClass
	 */
	public static void create(ProjectSetup... projects) throws Throwable {
		for (ProjectSetup project : projects) {
			project.before();
		}
	}

	/**
	 * This method implements workaround when using this class in JUnit before
	 * 4.9 (without &#64;ClassRule) and should be called from the method
	 * annotated with &#64;AfterClass
	 */
	public static void delete(ProjectSetup... projects) {
		for (ProjectSetup project : projects) {
			project.after();
		}
	}

	private final IWorkspaceSetup workspaceSetup;
	private final String projectName;
	private IProject project;
	private final Set<Option> options;

	public ProjectSetup(IWorkspaceSetup workspaceSetup, String projectName) {
		this.workspaceSetup = workspaceSetup;
		this.projectName = projectName;
		this.options = Collections.emptySet();
	}

	public ProjectSetup(IWorkspaceSetup workspaceSetup, String projectName,
			Option option, Option... restOptions) {
		this.workspaceSetup = workspaceSetup;
		this.projectName = projectName;
		this.options = new HashSet<>();
		this.options.add(option);
		Collections.addAll(this.options, restOptions);
		if (hasOption(Option.INDEXER_DISABLED)
				&& hasOption(Option.WAIT_INDEXES_READY)) {
			throw new IllegalStateException("Conflicting options: "
					+ TextUtils.join(Arrays.asList(Option.INDEXER_DISABLED,
							Option.WAIT_INDEXES_READY), ","));
		}
	}

	protected boolean hasOption(Option option) {
		return options.contains(option);
	}

	@Override
	protected boolean isVerbose() {
		return hasOption(Option.VERBOSE);
	}

	@Override
	protected void before() throws Throwable {
		workspaceSetup.before();
		if (hasOption(Option.INDEXER_DISABLED)) {
			ModelManager.getModelManager().getIndexManager().disable();
		}
		project = createProject(getProjectName());
		if (hasOption(Option.BUILD)) {
			final long start = System.currentTimeMillis();
			buildProject();
			if (isVerbose()) {
				System.out.println((System.currentTimeMillis() - start)
						+ " ms for full build of " + getProjectName()
						+ " project");
			}
		}
		if (hasOption(Option.WAIT_INDEXES_READY)) {
			ModelManager.getModelManager().getIndexManager().waitUntilReady();
		}
	}

	protected IProject createProject(String workspaceProjectName)
			throws IOException, CoreException {
		final File source = getSourceDirectory();
		if (!source.isDirectory()) {
			throw new IllegalStateException(
					NLS.bind("Source directory \"{0}\" doesn't exist", source));
		}
		final Set<File> excludes = new HashSet<>();
		for (Option option : options) {
			if (option instanceof ExcludeOption) {
				final File exclude = new File(source,
						((ExcludeOption) option).path);
				if (!exclude.exists()) {
					throw new IllegalStateException(NLS.bind(
							"Excluded file \"{0}\" doesn't exist", exclude));
				}
				excludes.add(exclude);
			}
		}
		final File target = getWorkspaceRoot().getLocation()
				.append(workspaceProjectName).toFile();
		FileUtil.copyDirectory(source, target, excludes);
		final IProject project = getWorkspaceRoot()
				.getProject(workspaceProjectName);
		ResourcesPlugin.getWorkspace().run(monitor -> {
			project.create(null);
			if (!hasOption(Option.CLOSED)) {
				project.open(null);
			}
		}, null);
		return project;
	}

	public File getSourceDirectory() {
		return new File(workspaceSetup.getSourceWorkspaceDirectory(),
				getSourceProjectName());
	}

	protected void buildProject() throws CoreException {
		get().build(IncrementalProjectBuilder.FULL_BUILD, null);
	}

	@Override
	protected void after() {
		if (project != null) {
			try {
				deleteProject(project);
			} catch (CoreException e) {
				e.printStackTrace();
			}
			project = null;
		}
		try {
			deleteProject(getWorkspaceRoot().getProject(getProjectName()));
		} catch (CoreException e) {
			e.printStackTrace();
		}
		if (hasOption(Option.INDEXER_DISABLED)) {
			ModelManager.getModelManager().getIndexManager().enable();
		}
		workspaceSetup.after();
	}

	private static void deleteProject(IProject project) throws CoreException {
		if (project.exists() && !project.isOpen()) {
			// force opening so that project can be deleted without
			// logging (see bug 23629)
			project.open(null);
		}
		AbstractModelTests.deleteResource(project);
	}

	/**
	 * Returns name of the project in the {@link #workspaceSetup source
	 * workspace}.
	 */
	public String getSourceProjectName() {
		return projectName;
	}

	/**
	 * Returns workspace name of the project.
	 */
	@Override
	public String getProjectName() {
		return projectName;
	}

	/**
	 * Returns this project as IProject
	 */
	@Override
	public IProject get() {
		Assert.assertNotNull(
				"ProjectSetup " + getProjectName() + " not initialized",
				project);
		return project;
	}

	/**
	 * Creates the specified file from the source project. Typical use case is
	 * creation of the files which were excluded initially.
	 *
	 * @param filename
	 *            project related filename
	 * @param option
	 *            {@link Option#BUILD} or <code>null</code>
	 * @throws CoreException
	 */
	public IFile createFile(String filename, Option option)
			throws CoreException {
		final File sourceFile = new File(getSourceDirectory(), filename);
		if (!sourceFile.isFile()) {
			throw new IllegalArgumentException(
					NLS.bind("Source file {0} doesn't exist", sourceFile));
		}
		final IFile file = getFile(filename);
		final FileInputStream input;
		try {
			input = new FileInputStream(sourceFile);
		} catch (FileNotFoundException e) {
			throw new IllegalArgumentException(e);
		}
		if (file.exists()) {
			file.setContents(input, IResource.NONE, null);
		} else {
			final IContainer parent = file.getParent();
			if (parent instanceof IFolder) {
				ResourceUtil.createFolder((IFolder) parent, null);
			}
			file.create(input, IResource.NONE, null);
		}
		if (option == ProjectSetup.Option.BUILD) {
			build();
		}
		return file;
	}

	/**
	 * Creates {@link RuleChain} initializing the specified rules in the
	 * specified order.
	 */
	public static RuleChain chainOf(TestRule first, TestRule second,
			TestRule... rest) {
		RuleChain chain = RuleChain.outerRule(first).around(second);
		for (TestRule rule : rest) {
			chain = chain.around(rule);
		}
		return chain;
	}

}