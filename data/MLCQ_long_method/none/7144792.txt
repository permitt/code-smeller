    public HttpResponse(int code, String message,Map<String, List<String>> headers,
                        String content) {
        this.code = code;
        this.message = message;
        this.headers = new HashMap<>(headers);
        this.content = content;
    }