	@Override
	/** {@inheritDoc} */
	public SubtypeConstraint intersection(final SubtypeConstraint other) {
		final StringSubtypeTreeElement o = (StringSubtypeTreeElement) other;
		if (o instanceof StringSetConstraint) {
			final StringSetConstraint ssc = (StringSetConstraint) o;
			if (ssc.constraintType == constraintType) {
				return new StringSetConstraint(stringType, constraintType,
						constraint.intersection(((StringSetConstraint) o).constraint));
			}
		}

		final StringSetOperation returnValue = new StringSetOperation(stringType, OperationType.INTERSECTION, this, o);
		return returnValue.evaluate();
	}