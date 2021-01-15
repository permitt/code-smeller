    private static ScheduledExecutorService createTimeoutCheckScheduler()
    {
        ThreadFactory threadFactory = newDaemonThreadFactory( "timeout-check-timer" );
        return newScheduledThreadPool( 1, threadFactory );
    }