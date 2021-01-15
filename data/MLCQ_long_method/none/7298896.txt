	@Override
	public void declareExchange(final Exchange exchange) {
		try {
			this.rabbitTemplate.execute(channel -> {
				declareExchanges(channel, exchange);
				return null;
			});
		}
		catch (AmqpException e) {
			logOrRethrowDeclarationException(exchange, "exchange", e);
		}
	}