  public int getParamCount(HplsqlParser.Expr_func_paramsContext ctx) {
    if (ctx == null) {
      return 0;
    }
    return ctx.func_param().size();
  }