  public Transmission(String connectionId, SocketChannel socketChannel, SelectionKey key, Time time,
      NetworkMetrics metrics) {
    this.connectionId = connectionId;
    this.socketChannel = socketChannel;
    this.key = key;
    this.time = time;
    this.metrics = metrics;
  }