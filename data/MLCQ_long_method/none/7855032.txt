  @Override
  public void removeHealthMonitor(InternalDistributedMember owner, int theId) {
    final HealthMonitor hm = getHealthMonitor(owner);
    if (hm != null && hm.getId() == theId) {
      hm.stop();
      this.hmMap.remove(owner);
    }
  }