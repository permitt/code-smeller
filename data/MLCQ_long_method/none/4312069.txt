    public static boolean isOid( String oidString )
    {
        try
        {
            Oid.fromString( oidString );

            return true;
        }
        catch ( DecoderException e )
        {
            return false;
        }
    }