  public UrlRewriteContextImpl(
      UrlRewriteEnvironment environment,
      Resolver resolver,
      Map<String,UrlRewriteFunctionProcessor> functions,
      UrlRewriter.Direction direction,
      Template url ) {
    this.environment = environment;
    this.resolver = resolver;
    this.functions = functions;
    this.params = new ContextParameters();
    this.evaluator = new ContextEvaluator();
    this.direction = direction;
    this.originalUrl = url;
    this.currentUrl = url;
  }