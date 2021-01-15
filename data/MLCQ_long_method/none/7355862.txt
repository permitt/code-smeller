    @Override
    public Object clone() throws CloneNotSupportedException {
        final HttpHost copy = (HttpHost) super.clone();
        copy.init(this);
        return copy;
    }