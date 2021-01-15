    FSDataBoundedInputStream(FileSystem fs, Path file, InputStream in) {
      super(in);
      this.fs = fs;
      this.file = file;
    }