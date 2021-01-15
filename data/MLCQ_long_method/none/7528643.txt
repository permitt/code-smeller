	public SqsMessageHandler(AmazonSQSAsync amazonSqs, ResourceIdResolver resourceIdResolver) {
		this(amazonSqs, new DynamicQueueUrlDestinationResolver(amazonSqs, resourceIdResolver));
	}