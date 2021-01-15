		private DeleteCommand(@Nullable ByteBuffer key, List<RecordId> recordIds) {

			super(key);
			this.recordIds = recordIds;
		}