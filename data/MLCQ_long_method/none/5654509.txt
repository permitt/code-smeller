    public void setAllowedColumns(final Set<Column> inclusion) {
        ArgumentChecks.ensureNonNull("inclusion", inclusion);
        columns.clear();
        columns.addAll(inclusion);
    }