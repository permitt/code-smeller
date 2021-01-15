    @Override
    public void println(char x) throws IOException
    {
        getEnclosingWriter().println(x);
    }