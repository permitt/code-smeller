        static Object checkValue(Object value) {
            if (value == null) {
                throw new IllegalArgumentException("Value must not be null");
            }
            return value;
        }