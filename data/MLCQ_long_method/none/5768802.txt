    @Override
    public void delete(final String key) {
        ReportExec execution = find(key);
        if (execution == null) {
            return;
        }

        delete(execution);
    }