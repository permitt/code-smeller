    @Override
    public void write(byte[] b) throws IOException {
      count += b.length;
      out.write(b);
    }