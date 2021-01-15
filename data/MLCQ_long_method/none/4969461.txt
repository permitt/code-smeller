    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (!(obj instanceof Quota))
            return false;
        Quota that = (Quota) obj;
        return (that.bound == this.bound) && (that.upper == this.upper);
    }