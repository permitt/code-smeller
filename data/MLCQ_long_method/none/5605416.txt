    @Override
    public IMXMLEventSpecifierNode getEventSpecifierNode(String name)
    {
        return eventNodeMap != null ? eventNodeMap.get(name) : null;
    }