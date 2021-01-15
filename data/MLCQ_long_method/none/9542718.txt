  @Override
  public KillTaskAttemptResponse killTaskAttempt(
      KillTaskAttemptRequest request) throws IOException {
    KillTaskAttemptResponse resp =
      recordFactory.newRecordInstance(KillTaskAttemptResponse.class);
    return resp;
  }