		public String getName()
		{
			String lowerResult = lower.getName();
			String upperResult = upper.getName();
			
			if (lowerResult != null) {
				if (upperResult != null) {
					return lowerResult + " merged with " + upperResult;
				} else {
					return lowerResult;
				}
			} else {
				if (upperResult != null) {
					return upperResult;
				} else {
					return null;
				}
			}
		}