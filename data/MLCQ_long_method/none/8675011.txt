    @Override public Collection<ClusterNode> mapPartitionToPrimaryAndBackups(int part) {
        CacheOperationContext old = gate.enter(null);

        try {
            return delegate.mapPartitionToPrimaryAndBackups(part);
        }
        finally {
            gate.leave(old);
        }
    }