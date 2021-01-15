    @Override
    protected void invoke( Class<?> c )
        throws Exception
    {
        getRuntime().getConstructors( c );
    }