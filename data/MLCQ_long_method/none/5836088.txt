    private String getUnquoted() {
        while (i < size) {
            parseLiteral();
            parseEL();
        }
        return result.toString();
    }