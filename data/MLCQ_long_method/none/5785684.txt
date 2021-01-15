  @Override
  public void toSummaryProtoStream(OutputStream outputStream) throws IOException {
    ProtoUtils.toSummaryEventProto(dagID, commitStartTime,
        getEventType(), null).writeDelimitedTo(outputStream);
  }