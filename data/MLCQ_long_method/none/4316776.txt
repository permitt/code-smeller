	public long update(long t)
	{
		counter = t;
		//		System.out.println("counter updated to " + this);
		initialized = true;
		return counter;
	}