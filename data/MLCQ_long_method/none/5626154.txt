	public boolean isSuspended() throws NotConnectedException
	{
		if (!isConnected())
			throw new NotConnectedException();

		return m_isHalted;
	}