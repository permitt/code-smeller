    public Interaction open() throws Exception
    {
        return _interaction.sendPerformative(new ConnectionOpenBody(AMQShortString.valueOf(_openVirtualHost),
                                                                    null,
                                                                    false));
    }