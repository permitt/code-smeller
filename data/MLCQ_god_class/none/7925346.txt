	public static class UpdateDataAssociationFeature extends AbstractBpmn2UpdateFeature {

		public UpdateDataAssociationFeature(IFeatureProvider fp) {
			super(fp);
		}

		@Override
		public boolean canUpdate(IUpdateContext context) {
			if (context.getPictogramElement() instanceof Connection) {
				return BusinessObjectUtil.getFirstElementOfType(
						context.getPictogramElement(), DataAssociation.class) != null;
			}
			return false;
		}

		@Override
		public IReason updateNeeded(IUpdateContext context) {
			if (canUpdate(context)) {
				Connection connection = (Connection) context.getPictogramElement();
				DataAssociation businessObject = BusinessObjectUtil.getFirstElementOfType(context.getPictogramElement(),
						DataAssociation.class);
				String newDirection = getDirection(businessObject);
				String oldDirection = FeatureSupport.getPropertyValue(connection, ASSOCIATION_DIRECTION);
				if (oldDirection==null || oldDirection.isEmpty())
					oldDirection = ""; //$NON-NLS-1$
	
				if (!oldDirection.equals(newDirection)) {
					return Reason.createTrueReason();
				}
			}
			return Reason.createFalseReason();
		}

		@Override
		public boolean update(IUpdateContext context) {
			if (canUpdate(context)) {
				Connection connection = (Connection) context.getPictogramElement();
				DataAssociation businessObject = BusinessObjectUtil.getFirstElementOfType(context.getPictogramElement(),
						DataAssociation.class);
				setAssociationDirection(connection, businessObject);
				reconcileDataTypes(connection, businessObject);
			}
			return true;
		}

		/**
		 * @param connection
		 * @param businessObject
		 */
		private void reconcileDataTypes(Connection connection, DataAssociation assoc) {
			if (assoc.getSourceRef().size()==1 && assoc.getTargetRef()!=null) {
				ItemAwareElement source = assoc.getSourceRef().get(0);
				ItemAwareElement target = assoc.getTargetRef();
				ItemDefinition sourceType = source.getItemSubjectRef();
				ItemDefinition targetType = target.getItemSubjectRef();
				if (sourceType!=null) {
//					if (target.getItemSubjectRef()==null)
						target.setItemSubjectRef(sourceType);
					
				}
				else if (targetType!=null) {
					source.setItemSubjectRef(targetType);
				}
			}
		}
	}