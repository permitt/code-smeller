		@Override
		protected void handleError(Exception exception) {
			if (!(exception instanceof RollbackException))
				super.handleError(exception);
		}