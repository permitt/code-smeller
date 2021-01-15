	private long allocateNewBlock(Nd nd, int blockSize) {
		short poolId = getMemoryPoolId(nd);
		int elementSize = getElementSize();
		long bytesNeeded = BlockHeader.BLOCK_HEADER_BYTES + blockSize * elementSize;
		// If we're close enough to filling the chunk that we wouldn't be able to fit any more elements anyway, allocate
		// the entire chunk. Although it wastes a small amount of space, it ensures that the blocks can be more easily
		// reused rather than being fragmented. It also allows freed blocks to be merged via the large block allocator.
		if (MAX_BYTES_IN_A_CHUNK - bytesNeeded < elementSize) {
			bytesNeeded = MAX_BYTES_IN_A_CHUNK;
		}
		long result = nd.getDB().malloc(bytesNeeded, poolId);
		BlockHeader.BLOCK_SIZE.put(nd, result, (short) blockSize);
		return result;
	}