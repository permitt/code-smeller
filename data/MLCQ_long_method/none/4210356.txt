    @Override
    public String shortDisplay()
    {
        return (happy() ? "[" : "") + name + "(?)" + (happy() ? "]" : "");
    }