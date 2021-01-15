    @Deprecated
    public AmazonS3EncryptionClient(AWSCredentials credentials,
            EncryptionMaterialsProvider encryptionMaterialsProvider) {
        this(credentials, encryptionMaterialsProvider,
                configFactory.getConfig(), new CryptoConfiguration());
    }