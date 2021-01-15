	private ColorHandle doGetColorHandle( String memberName )
	{
		return new ColorHandle( getElementHandle( ), StructureContextUtil
				.createStructureContext( this, memberName ) );
	}