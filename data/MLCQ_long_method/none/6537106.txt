    @Override
    public boolean supportsSensorType(SensorEnum sensorType) {
        if (sensorType != null) {
            return getSensorTypes().contains(sensorType);
        }
        return false;
    }