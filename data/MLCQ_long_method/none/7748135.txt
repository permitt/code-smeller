        private boolean containsDownEntity(Set<Entity> seeds) {
            for (Entity seed : seeds) {
                if (!isViableSeed(seed)) {
                    return true;
                }
            }
            return false;
        }