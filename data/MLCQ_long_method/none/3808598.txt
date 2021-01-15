      @Override
      public void run() {
         try {
            callOnMessage();
         } catch (Exception e) {
            ActiveMQClientLogger.LOGGER.onMessageError(e);

            lastException = e;
         }
      }