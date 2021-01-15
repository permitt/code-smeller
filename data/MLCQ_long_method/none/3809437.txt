   @Override
   public int readInt() throws JMSException {
      if (ActiveMQRALogger.LOGGER.isTraceEnabled()) {
         ActiveMQRALogger.LOGGER.trace("readInt()");
      }

      return ((BytesMessage) message).readInt();
   }