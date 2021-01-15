	public synchronized static ColorPalette getInstance( )
	{
		if ( instance == null )
		{
			instance = new ColorPalette( );
		}
		return instance;
	}