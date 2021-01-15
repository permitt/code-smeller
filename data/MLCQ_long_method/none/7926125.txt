		@Override
		public IReason updateNeeded(IUpdateContext context) {
			if (canUpdate(context)) {
				Connection connection = (Connection) context.getPictogramElement();
				Association businessObject = BusinessObjectUtil.getFirstElementOfType(context.getPictogramElement(),
						Association.class);
				String newDirection = businessObject.getAssociationDirection().toString();
				if (newDirection==null || newDirection.isEmpty())
					newDirection = AssociationDirection.NONE.toString();
				String oldDirection = FeatureSupport.getPropertyValue(connection, ASSOCIATION_DIRECTION);
				if (oldDirection==null || oldDirection.isEmpty())
					oldDirection = AssociationDirection.NONE.toString();
	
				if (!oldDirection.equals(newDirection)) {
					return Reason.createTrueReason(Messages.AssociationFeatureContainer_Direction_Changed);
				}
			}
			return Reason.createFalseReason();
		}