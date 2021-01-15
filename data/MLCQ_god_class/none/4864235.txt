    private static final class RequestCounter extends CacheStatsMBeanCounter {

        RequestCounter(CacheStatsMBean stats) {
            super(stats, REQUEST);
        }

        @Override
        public long getCount() {
            return stats.getRequestCount();
        }
    }