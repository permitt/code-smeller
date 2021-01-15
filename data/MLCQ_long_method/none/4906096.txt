    public int getRestrictionType(String restrictionName) {
        if (restrictions.containsKey(restrictionName)) {
            return restrictions.get(restrictionName);
        } else {
            return PropertyType.UNDEFINED;
        }
    }