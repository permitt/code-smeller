    @Override
    public boolean hasNext() {
        try {
            return !rs.isLast();
        } catch (final SQLException e) {
            rethrow(e);
            return false;
        }
    }