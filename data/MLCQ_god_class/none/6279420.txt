	static final class Slice {
		final int beginIndex;
		final int endIndex;

		Slice(int b, int e) {
			beginIndex = b;
			endIndex = e;
		}

		final int size() {
			return endIndex - beginIndex;
		}
	}