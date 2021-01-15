  public static void main(String args[]) throws UIMAException, IOException, URISyntaxException
  {
    if (args.length != 2)
    {
      System.err.format("Syntax: %s input_directory output_directory%n", RunZoner.class.getName());
    }
    
    File inputDirectory = new File(args[0]);
    File outputDirectory = new File(args[1]);
    
    List<File> inputFiles = listContentsAll(inputDirectory);
    
    RunZoner runner = new RunZoner();
    runner.setInputDirectory(inputDirectory);
    runner.setInputFiles(inputFiles);
    runner.setOutputDirectory(outputDirectory);
    
    runner.execute();
  }