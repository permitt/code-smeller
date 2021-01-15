    @Override public void restartNodes(Collection<UUID> ids) throws IgniteException {
        guard();

        try {
            ctx.grid().compute(forNodeIds(ids)).execute(IgniteKillTask.class, true);
        }
        finally {
            unguard();
        }
    }