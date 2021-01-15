	@Override
	public Supplier<MultiValueMap<K, V>> supplier() {
		return () -> CollectionUtils.toMultiValueMap(new HashMap<>());
	}