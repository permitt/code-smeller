    public String getMessage() {
        if (minor == 0)
            return (getMajorString());

        return (getMajorString()
                + " (Mechanism level: " + getMinorString() + ")");
    }