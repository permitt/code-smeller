    public Optional<UserEntity> getUser ( final String userId )
    {
        return Optional.ofNullable ( this.userMap.get ( userId ) );
    }