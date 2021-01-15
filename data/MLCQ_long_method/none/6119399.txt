    @Override
    public boolean allSatisfy(Predicate<? super T> predicate)
    {
        return this.delegate.allSatisfy(new SelectAllSatisfyPredicate<>(this.predicate, predicate));
    }