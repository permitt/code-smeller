    @Override
    @SuppressWarnings("CloneDoesntCallSuperClone")
    public final Matrix clone() {
        return Matrices.copy(this);
    }