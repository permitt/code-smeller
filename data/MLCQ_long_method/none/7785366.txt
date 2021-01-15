		protected final void doSelect(final int index)
		{
			String value = getChoiceValueForIndex(index);
			assignValueToFormComponent(formComponent, value);
		}