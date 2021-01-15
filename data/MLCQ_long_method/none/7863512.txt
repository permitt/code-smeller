  @Override
  public void removeAsyncEventQueueId(String asyncEventQueueId) {
    super.removeAsyncEventQueueId(asyncEventQueueId);
    new UpdateAttributesProcessor(this).distribute();
  }