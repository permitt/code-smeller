  @Override
  public void afterUpdate(EntryEvent<K, V> event) {
    addEvent(event);
    try {
      afterUpdate2(event);
    } catch (VirtualMachineError e) {
      SystemFailure.initiateFailure(e);
      throw e;
    } catch (Throwable t) {
      this.callbackError = t;
    }
  }