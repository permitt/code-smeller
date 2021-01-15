		protected void rollback( )
		{
			data.setAlias( originalAlias );
			data.setRealDisplayName( originalDisplayName );
			data.setDisplayNameKey( originalDisplayNameKey );
		}