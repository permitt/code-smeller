    @Override
    public synchronized int read() throws IOException {
      int data = blockInputStream.read();
      return data;
    }