	public static class PushInfo {

		private String pushRefSpec;
		private String pushUri;

		/**
		 * @param pushRefSpec
		 * @param pushUri
		 */
		public PushInfo(String pushRefSpec, String pushUri) {
			this.pushRefSpec = pushRefSpec;
			this.pushUri = pushUri;
		}

		/**
		 * @return the push ref spec
		 */
		public String getPushRefSpec() {
			return pushRefSpec;
		}

		/**
		 * @return the push URI
		 */
		public String getPushUri() {
			return pushUri;
		}
	}