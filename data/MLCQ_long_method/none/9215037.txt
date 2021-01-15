    public ProfileBranchNode(ResolvedJavaMethod method, int freqLog, int probabilityLog, int bci, int targetBci) {
        super(TYPE, method, freqLog, probabilityLog);
        assert targetBci <= bci;
        this.branchCondition = null;
        this.bci = bci;
        this.targetBci = targetBci;
    }