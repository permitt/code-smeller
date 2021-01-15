    @Override
    public InstancesResult resumeInstances(Entity entity, Date start, Date end,
                                           Properties props, List<LifeCycle> lifeCycles) throws FalconException {
        return doJobAction(JobAction.RESUME, entity, start, end, props, lifeCycles);
    }