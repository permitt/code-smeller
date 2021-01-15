    protected Builder(InputFile file) {
      this.readSupport = null;
      this.file = checkNotNull(file, "file");
      this.path = null;
      if (file instanceof HadoopInputFile) {
        this.conf = ((HadoopInputFile) file).getConfiguration();
      } else {
        this.conf = new Configuration();
      }
      optionsBuilder = HadoopReadOptions.builder(conf);
    }