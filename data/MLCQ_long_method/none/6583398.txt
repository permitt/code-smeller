	public final boolean equals(final Object object) {
		if (object instanceof LegacyViewContributionExpression) {
			final LegacyViewContributionExpression that = (LegacyViewContributionExpression) object;
			return equals(this.activePartId, that.activePartId)
					&& equals(this.getWindow(), that.getWindow());
		}

		return false;
	}