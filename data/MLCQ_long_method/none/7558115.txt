	public OperationResponse create(HttpStatus status, HttpHeaders headers,
			byte[] content) {
		return new StandardOperationResponse(status, augmentHeaders(headers, content),
				content);
	}