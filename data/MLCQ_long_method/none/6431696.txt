    @Override
    public String toString() {
        return MoreObjects.toStringHelper(this)
            .add("Affected", affected)
            .add("AffectedType", affectedType)
            .add("Verb", verb)
            .toString();
    }