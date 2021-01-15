	public void parse(  ) throws ParseException
	{
		try
		{
			parser.open( templateDir );
		}
		catch ( FileNotFoundException e )
		{
			return;
		}

		parseElement( );
	}