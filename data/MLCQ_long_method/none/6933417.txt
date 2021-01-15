  @Override
  protected void consumeAttributes(AttributeHelper helper) throws ParseException
      {
    total = helper.consumeInteger(TOTAL, false);
    value = helper.consumeBoolean(null, false);
  }