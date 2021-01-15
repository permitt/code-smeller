	public static final double computeWidth( IDisplayServer xs, Label la )
	{
		final ITextMetrics itm = xs.getTextMetrics( la );
		try
		{
			return computeWidth( itm, la );
		}
		finally
		{
			itm.dispose( );
		}
	}