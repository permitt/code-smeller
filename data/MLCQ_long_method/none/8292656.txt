        public Builder username(String username) {
            Preconditions.checkState(!this.username.isPresent());

            this.username = Optional.of(username);
            return this;
        }