		@Override
		public void checkWants(UploadPack up, List<ObjectId> wants)
				throws PackProtocolException, IOException {
			checkNotAdvertisedWants(up, wants,
					refIdSet(up.getAdvertisedRefs().values()));
		}