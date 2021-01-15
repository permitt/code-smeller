    @Specialization
    protected RIntVector match(RAbstractRawVector x, @SuppressWarnings("unused") RAbstractComplexVector table, @SuppressWarnings("unused") int nomatch) {
        return RDataFactory.createIntVector(x.getLength(), true);
    }