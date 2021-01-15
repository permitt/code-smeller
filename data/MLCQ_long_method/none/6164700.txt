  @Inject
  public UsagesNode(
      @Assisted UsagesResponse response,
      NodeFactory nodeFactory,
      PromiseProvider promiseProvider,
      TreeStyles styles,
      JavaResources resources) {
    this.response = response;
    this.nodeFactory = nodeFactory;
    this.promiseProvider = promiseProvider;
    this.resources = resources;
    this.styles = styles;
  }