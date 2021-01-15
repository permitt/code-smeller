    @Override
    public Integer getOkResponse() {
        Optional<Integer> propertyValue = getProperty(DialogConditionType.OK_RESPONSE);
        return propertyValue.orElse(null);
    }