    private UUID cacheIfNecessary(final UUID candidate)
    {
        UUID existing = _uuids.putIfAbsent(candidate, candidate);
        return existing == null ? candidate : existing;
    }