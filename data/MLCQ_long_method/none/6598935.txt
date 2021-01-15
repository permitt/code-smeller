    public void logAction(String actionName, LogLevels level) {
        toLog(format(shortLogMessagesFormat
                ? "%s for %s"
                : "Perform action '%s' with Element (%s)", actionName, this.toString()), level);
    }