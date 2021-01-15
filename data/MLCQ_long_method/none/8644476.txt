    ZkDiscoveryNodeJoinEventData(
        long evtId,
        long topVer,
        List<ZkJoinedNodeEvtData> joinedNodes,
        int dataForJoinedPartCnt)
    {
        super(evtId, ZK_EVT_NODE_JOIN, topVer);

        this.joinedNodes = joinedNodes;
        this.dataForJoinedPartCnt = dataForJoinedPartCnt;
    }