    @Override public void clear() {
        if (delegate == null)
            delegate = new ArrayList<>();
        else
            delegate.clear();
    }