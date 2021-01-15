    public static ValueNode create(ValueNode forValue, ConstantReflectionProvider constantReflection) {
        if (forValue instanceof NewArrayNode) {
            NewArrayNode newArray = (NewArrayNode) forValue;
            return newArray.length();
        }

        ValueNode length = readArrayLength(forValue, constantReflection);
        if (length != null) {
            return length;
        }
        return new ArrayLengthNode(forValue);
    }