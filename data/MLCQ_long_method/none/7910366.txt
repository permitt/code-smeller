  public static TProtocol newProtocolInstance(ThriftProtocol protocol, TTransport transport) {
    return getProtocolFactory(protocol).getProtocol(transport);
  }