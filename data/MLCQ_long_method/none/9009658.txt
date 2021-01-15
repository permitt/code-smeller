  public PeerSyncWithLeader(SolrCore core, String leaderUrl, int nUpdates) {
    this.core = core;
    this.leaderUrl = leaderUrl;
    this.nUpdates = nUpdates;

    this.doFingerprint = !"true".equals(System.getProperty("solr.disableFingerprint"));
    this.uhandler = core.getUpdateHandler();
    this.ulog = uhandler.getUpdateLog();
    HttpClient httpClient = core.getCoreContainer().getUpdateShardHandler().getDefaultHttpClient();
    this.clientToLeader = new HttpSolrClient.Builder(leaderUrl).withHttpClient(httpClient).build();

    this.updater = new PeerSync.Updater(msg(), core);

    core.getCoreMetricManager().registerMetricProducer(SolrInfoBean.Category.REPLICATION.toString(), this);
  }