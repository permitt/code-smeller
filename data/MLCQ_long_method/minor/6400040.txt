    private void setPropertyValue(Object object, String propertyName, Object value) {
        assert object != null : "object can not be null!"; //$NON-NLS-1$

        try {
            Object singlePropertyObject = null;
            String singlePropertyName = null;
            if (propertyName.contains(".")) { //$NON-NLS-1$
                singlePropertyObject = getPropertyValue(
                        object,
                        propertyName.substring(0, propertyName.lastIndexOf("."))); //$NON-NLS-1$
                singlePropertyName = propertyName.substring(propertyName.lastIndexOf(".") + 1); //$NON-NLS-1$
            } else {
                singlePropertyObject = object;
                singlePropertyName = propertyName;
            }

            String setterName = "set" //$NON-NLS-1$
                    + singlePropertyName.substring(0, 1).toUpperCase()
                    + singlePropertyName.substring(1);
            Method setterMethod = null;
            if (value != null) {
                setterMethod = singlePropertyObject.getClass().getMethod(
                        setterName, new Class<?>[] { value.getClass() });
            } else {
                // as the value is null we can not access the setter method
                // directly and have to search for the method
                Method[] methods = singlePropertyObject.getClass().getMethods();
                for (Method m : methods) {
                    if (m.getName().equals(setterName)) {
                        setterMethod = m;
                    }
                }
            }
            setterMethod.invoke(singlePropertyObject, value);
        } catch (Exception e) {
            log.error("Error on reflective accessing the data model", e); //$NON-NLS-1$
            throw new RuntimeException(e);
        }
    }