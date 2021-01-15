  @Override
  public void handleFailedContainer(TaskAttemptId attemptID) {
    toBePreempted.remove(attemptID);
    checkpoints.remove(attemptID.getTaskId());
  }