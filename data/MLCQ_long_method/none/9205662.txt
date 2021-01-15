	private void setDataType( StyleEntry entry, Object value, String dataLocale )
	{
		ULocale locale = getLocale( dataLocale );
		setDataType( entry, value, locale );
	}