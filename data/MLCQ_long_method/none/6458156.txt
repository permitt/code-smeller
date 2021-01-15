    public InstantTypeAdapter ( final DateTimeFormatter formatter )
    {
        this.formatter = formatter.withLocale ( Locale.US );
    }