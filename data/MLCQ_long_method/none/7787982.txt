	public static Behavior findBehavior(Component component, Class<? extends Behavior> behaviorClass)
	{
		for (Behavior behavior : component.getBehaviors(behaviorClass))
		{
			return behavior;
		}
		return null;
	}