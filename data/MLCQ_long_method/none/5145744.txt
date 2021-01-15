    public String getStdErr()
    {
        StringBuilder str = new StringBuilder();
        for ( String line : stderr )
        {
            str.append( line );
        }
        return str.toString();
    }