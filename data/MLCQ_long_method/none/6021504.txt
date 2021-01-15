        @JsonCreator
        public UsernamePasswordAuthentication(
            @JsonProperty("username") String username,
            @JsonProperty("password") String password) {
            this.password = password;
            this.username = username;
        }