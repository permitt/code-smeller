    private ProgressNotificationEditor(Editor editor, String path, Function<String, Void> onProgress) {
        this.editor = editor;
        this.path = path;
        this.onProgress = onProgress;
    }