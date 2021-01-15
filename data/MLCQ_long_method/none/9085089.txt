		@Override
		public Void visitLong(long i, Void p)
		{
			if (i == 300L) {
				_visited.add(Visited.LONG);
			}
			return null;
		}