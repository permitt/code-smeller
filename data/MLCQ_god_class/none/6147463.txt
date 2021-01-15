	private static class LineTrackerBuilder extends LineSplitter {

		public LineTrackerBuilder(CharSequence content) {
			super(content);
		}

		public ISourceLineTracker buildLineTracker() {
			final List<String> delimiters = new ArrayList<>();
			IntList lineOffsets = new IntList(256);
			contentPos = 0;
			while (contentPos < contentEnd) {
				final int begin = contentPos;
				findEndOfLine();
				lineOffsets.add(begin);
				delimiters.add(lastLineDelimiter);
			}
			return new DefaultSourceLineTracker(contentEnd,
					lineOffsets.toArray(),
					delimiters.toArray(new String[delimiters.size()]));
		}

	}