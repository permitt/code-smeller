	private void destroyBeanFactoryLocator() {
		Optional.ofNullable(getBeanFactoryLocator()).ifPresent(GemfireBeanFactoryLocator::destroy);
		this.beanFactoryLocator = null;
	}