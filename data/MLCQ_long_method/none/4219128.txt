    public void onRemove(InetAddressAndPort endpoint)
    {
        convict(endpoint, Double.MAX_VALUE);
    }