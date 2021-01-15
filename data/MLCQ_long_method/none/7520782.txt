	@Override
	public SecurityConfigurer<I> namenodePrincipal(String principal) {
		if (StringUtils.hasText(principal)) {
			hadoopSecurity.setNamenodePrincipal(principal);
		}
		return this;
	}