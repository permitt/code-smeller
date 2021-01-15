    @Override
    public boolean contains(String documentName) {
        requireNonNull(documentName, "documentName is required");
        return documents.containsKey(documentName);
    }