	public static class FeatureRankAsc implements Comparator<FeatureRank> {

		@Override
		public int compare(FeatureRank o1, FeatureRank o2) {
			if (o1.getEvaluation() > o2.getEvaluation()) {
				return 1;
			} else if (o1.getEvaluation() == o2.getEvaluation()) {
				return o1.getFeatureName().compareTo(o2.getFeatureName());
			} else {
				return -1;
			}
		}
	}