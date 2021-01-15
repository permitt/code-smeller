public class GoldEventPrinterWithLabels {

  static interface Options {

    @Option(longName = "xmi-dir")
    public File getInputDirectory();

    @Option(longName = "patients")
    public CommandLine.IntegerRanges getPatients();

    @Option(longName = "output-train")
    public File getTrainOutputDirectory();

    @Option(longName = "output-test")
    public File getTestOutputDirectory();
  }

  public static void main(String[] args) throws Exception {

    Options options = CliFactory.parseArguments(Options.class, args);

    File trainFile = options.getTrainOutputDirectory();
    if(trainFile.exists()) {
      trainFile.delete();
    }
    trainFile.createNewFile();
    File devFile = options.getTestOutputDirectory();
    if(devFile.exists()) {
      devFile.delete();
    }
    devFile.createNewFile();

    List<Integer> patientSets = options.getPatients().getList();
    List<Integer> trainItems = THYMEData.getPatientSets(patientSets, THYMEData.TRAIN_REMAINDERS);
    List<Integer> devItems = THYMEData.getPatientSets(patientSets, THYMEData.DEV_REMAINDERS);

    List<File> trainFiles = Utils.getFilesFor(trainItems, options.getInputDirectory());
    List<File> devFiles = Utils.getFilesFor(devItems, options.getInputDirectory());

    // sort training files to eliminate platform specific dir listings
    Collections.sort(trainFiles);

    // write training data to file
    CollectionReader trainCollectionReader = Utils.getCollectionReader(trainFiles);
    AnalysisEngine trainDataWriter = AnalysisEngineFactory.createEngine(
        EventPrinter.class,
        "OutputFile",
        trainFile.getAbsoluteFile());
    SimplePipeline.runPipeline(trainCollectionReader, trainDataWriter);

    // write dev data to file
    CollectionReader devCollectionReader = Utils.getCollectionReader(devFiles);
    AnalysisEngine devDataWriter = AnalysisEngineFactory.createEngine(
        EventPrinter.class,
        "OutputFile",
        devFile.getAbsolutePath());
    SimplePipeline.runPipeline(devCollectionReader, devDataWriter);
  }

  /**
   * Print events and entities.
   *  
   * @author dmitriy dligach
   */
  public static class EventPrinter extends JCasAnnotator_ImplBase {

    @ConfigurationParameter(
        name = "OutputFile",
        mandatory = true,
        description = "path to the output file")
    private String outputFile;

    @Override
    public void process(JCas jCas) throws AnalysisEngineProcessException {

      // gold EventMention(s) are all in gold view
      JCas goldView;
      try {
        goldView = jCas.getView("GoldView");
      } catch (CASException e) {
        throw new AnalysisEngineProcessException(e);
      }

      // system view has sentence segmentation, tokens, and dictionary lookup events
      JCas systemView;
      try {
        systemView = jCas.getView("_InitialView");
      } catch (CASException e) {
        throw new AnalysisEngineProcessException(e);
      }

      List<String> labelsAndTokens = new ArrayList<>();
      for(Sentence sentence : JCasUtil.select(systemView, Sentence.class)) {
        List<String> sentenceTokens = new ArrayList<>(); // tokens in this sentence
        List<String> sentenceLabels = new ArrayList<>(); // label for each token in this sentence 
        
        for(BaseToken baseToken : JCasUtil.selectCovered(systemView, BaseToken.class, sentence)) {
          sentenceTokens.add(tokenToString(baseToken));
          List<EventMention> events = JCasUtil.selectCovering(goldView, EventMention.class, baseToken.getBegin(), baseToken.getEnd());
          if(events.size() > 0) {
            sentenceLabels.add("1"); // this is an event
          } else {
            sentenceLabels.add("0"); // this is not an event
          }
        }

        String sentenceAsString = String.join(" ", sentenceTokens).replaceAll("[\r\n]", " ");
        String labelsAsString = String.join(" ", sentenceLabels);
        labelsAndTokens.add(labelsAsString + "|" + sentenceAsString);
      }

      try {
        Files.write(Paths.get(outputFile), labelsAndTokens, StandardOpenOption.APPEND);
      } catch (IOException e) {
        e.printStackTrace();
      }
    }
  }

  /*
   * Make sure this matches how data was pre-processed for word2vec
   */
  public static String tokenToString(BaseToken token) {

    String stringValue;
    String tokenType = token.getClass().getSimpleName();
    String tokenText = token.getCoveredText().toLowerCase();

    switch(tokenType) {
    case "ContractionToken":
      stringValue = tokenText;
      break;
    case "NewlineToken":
      // stringValue = null;
      stringValue = "";
      break;
    case "NumToken":
      stringValue = "number_token";
      break;
    case "PunctuationToken":
      stringValue = tokenText;
      break;
    case "SymbolToken":
      stringValue = tokenText;
      break;
    case "WordToken":
      stringValue = tokenText;
      break;
    default:
      throw new IllegalArgumentException("Invalid token type: " + tokenType);
    }

    return stringValue;
  }
}