  public static KeyValue createKeyValueFromKey(final ByteBuffer bb) {
    return createKeyValueFromKey(bb.array(), bb.arrayOffset(), bb.limit());
  }