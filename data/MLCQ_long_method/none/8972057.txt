  @Override
  public void deleteDocByQuery(String query) {
    if(docBuilder != null){
      docBuilder.writer.deleteByQuery(query);
    } 
  }