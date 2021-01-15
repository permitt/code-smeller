  public void applicationFinished(ApplicationId applicationId) {
    processDelegationTokenRenewerEvent(new DelegationTokenRenewerEvent(
        applicationId,
        DelegationTokenRenewerEventType.FINISH_APPLICATION));
  }