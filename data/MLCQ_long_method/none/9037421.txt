	void chunkDirtied(final Chunk chunk) {
		if (chunk.fSequenceNumber < NUM_HEADER_CHUNKS) {
			return;
		}
		this.dirtyChunkSet.add(chunk);
	}