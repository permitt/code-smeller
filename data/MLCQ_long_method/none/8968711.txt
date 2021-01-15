    @Override
    public int hashCode() {
      List<Object> list = new ArrayList<Object>();

      boolean present_success = true;
      list.add(present_success);
      if (present_success)
        list.add(success);

      return list.hashCode();
    }