		@Override
		public final Builder sslContext(SslContext sslContext){
			this.sslContext = Objects.requireNonNull(sslContext, "sslContext");
			return this;
		}