	public EList<Trigger> getTriggers( )
	{
		if ( triggers == null )
		{
			triggers = new EObjectContainmentEList<Trigger>( Trigger.class,
					this,
					ComponentPackage.MARKER_RANGE__TRIGGERS );
		}
		return triggers;
	}