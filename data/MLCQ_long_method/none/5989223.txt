    @BeforeClass
    public static void setUp() throws Exception {
        s3 = s3ClientBuilder().build();
        s3Async = s3AsyncClientBuilder().build();
    }