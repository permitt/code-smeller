    public UsernamePasswordCredentials(final String username, final String password) {
        super();

        if (username == null) {
            throw new IllegalArgumentException("Username may not be null");
        }

        this.username = username;
        this.password = password;
    }