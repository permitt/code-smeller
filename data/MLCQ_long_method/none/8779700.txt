    @Override
    public void setKeyComparator(Class<? extends WritableComparator> cmpcl) {
      super.setKeyComparator(cmpcl);
      for (Node n : kids) {
        n.setKeyComparator(cmpcl);
      }
    }