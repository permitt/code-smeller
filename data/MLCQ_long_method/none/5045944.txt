    public RDFParserBuilder fromString(String string) {
        clearSource();
        this.content = string;
        return this;
    }