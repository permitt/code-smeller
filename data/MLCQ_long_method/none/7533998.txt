	public Object aggregate(Collection<Object> results) {
		for (Object o : results) {
			if (o instanceof MessagingException) {
				return new ConsolidatedResultsException(results);
			}
		}
		return results;
	}