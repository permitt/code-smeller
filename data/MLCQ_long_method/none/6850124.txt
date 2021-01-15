  public CGraphPanelSynchronizer(final CGraphModel model, final CGraphWindowMenuBar menuBar) {
    m_model = Preconditions.checkNotNull(model, "IE01618: Model argument can not be null");
    m_menuBar = Preconditions.checkNotNull(menuBar, "IE01620: Menu bar argument can not be null");

    m_clickHandler = new CNodeClickHandler(model);

    m_model.getGraph().addListener(m_graphListener);
    m_model.getGraph().getRawView().addListener(m_viewListener);
  }