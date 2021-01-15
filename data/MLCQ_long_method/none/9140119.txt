	public void addElementEvent( DesignElementHandle focus, NotificationEvent ev )
	{
		ModelEventInfo event = new ModelEventInfo( focus, ev );
		eventList.add( event );
	}