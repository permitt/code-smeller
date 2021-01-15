		@Nonnull
		@Override
		public TypeSerializerSchemaCompatibility<T> setPreviousSerializerSnapshotForRestoredState(
				TypeSerializerSnapshot<T> previousSerializerSnapshot) {
			throw new UnsupportedOperationException("The snapshot of the state's previous serializer has already been set; cannot reset.");
		}