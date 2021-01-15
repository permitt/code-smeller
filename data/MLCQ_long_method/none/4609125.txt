	@Override
	public int hashCode() {
		Preconditions.checkNotNull(type, "TypeInformation type class is required");

		return type.hashCode();
	}