    public int hashCode() {
        if (hashCode == HASH_INITIAL) {
            hashCode = hashCode * HASH_FACTOR
                    + Util.hashCode(activityRequirementBindings);
            hashCode = hashCode * HASH_FACTOR
                    + Util.hashCode(activityPatternBindings);
            hashCode = hashCode * HASH_FACTOR + Util.hashCode(defined);
            hashCode = hashCode * HASH_FACTOR + Util.hashCode(enabled);
            hashCode = hashCode * HASH_FACTOR + Util.hashCode(id);
            hashCode = hashCode * HASH_FACTOR + Util.hashCode(name);
            if (hashCode == HASH_INITIAL) {
				hashCode++;
			}
        }

        return hashCode;
    }