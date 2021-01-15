    public int forceCompletionOfGroup(String key) {
        if (processor != null) {
            return processor.forceCompletionOfGroup(key);
        } else {
            return 0;
        }
    }