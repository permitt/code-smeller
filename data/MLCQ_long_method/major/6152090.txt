	public boolean matchesName(char[] pattern, char[] name) {
		if (pattern == null)
			return true; // null is as if it was "*"
		if (name != null) {
			boolean isCaseSensitive = (this.matchRule & R_CASE_SENSITIVE) != 0;
			boolean isCamelCase = (this.matchRule & R_CAMELCASE_MATCH) != 0;
			int matchMode = this.matchRule & MODE_MASK;
			boolean emptyPattern = pattern.length == 0;
			if (matchMode == R_PREFIX_MATCH && emptyPattern)
				return true;
			boolean sameLength = pattern.length == name.length;
			boolean canBePrefix = name.length >= pattern.length;
			boolean matchFirstChar = !isCaseSensitive || emptyPattern
					|| (name.length > 0 && pattern[0] == name[0]);
			if (isCamelCase && matchFirstChar
					&& CharOperation.camelCaseMatch(pattern, name)) {
				return true;
			}
			switch (matchMode) {
			case R_EXACT_MATCH:
			case R_FULL_MATCH:
				if (!isCamelCase) {
					if (sameLength && matchFirstChar) {
						return CharOperation.equals(pattern, name,
								isCaseSensitive);
					}
					break;
				}
				// fall through next case to match as prefix if camel case
				// failed
			case R_PREFIX_MATCH:
				if (canBePrefix && matchFirstChar) {
					return CharOperation.prefixEquals(pattern, name,
							isCaseSensitive);
				}
				break;
			case R_PATTERN_MATCH:
				if (!isCaseSensitive)
					pattern = CharOperation.toLowerCase(pattern);
				return CharOperation.match(pattern, name, isCaseSensitive);
			case R_REGEXP_MATCH:
				if (regexpCompiledPattern == null) {
					regexpCompiledPattern = Pattern.compile(
							new String(pattern), isCaseSensitive ? 0
									: Pattern.CASE_INSENSITIVE);
				}
				return regexpCompiledPattern.matcher(new String(name))
						.matches();
			}
		}
		return false;
	}