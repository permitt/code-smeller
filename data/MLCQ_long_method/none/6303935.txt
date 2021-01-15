    public void directUpgrade()
    {
        if (state != State.PREFACE)
            throw new IllegalStateException();
        prefaceParser.directUpgrade();
    }