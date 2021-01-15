	@Override
	public String convertToString(Object parameterValue)
			throws ParameterValueConversionException {
		if (!(parameterValue instanceof Integer)) {
			throw new ParameterValueConversionException("Invalid object type: "
					+ parameterValue);
		}
		Integer val = (Integer) parameterValue;
		return val.toString();
	}