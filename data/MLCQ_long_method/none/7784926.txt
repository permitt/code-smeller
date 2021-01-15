		public void supportSessionSerialization(ISerializer serializer)
		{
			this.serializer = Args.notNull(serializer, "serializer");
		}