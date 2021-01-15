	protected void prepare(final String prepareScript,
			final String prepareScriptDelimiter,
			final Map<String, Object> params) {
		if (prepareScript != null && prepareScript.length() > 0) {
			String[] statements = prepareScript.split(prepareScriptDelimiter);
			// throw out empty lines
			for (String sql : statements) {
				if (sql != null && sql.trim().length() > 0) {
					this.namedJdbcTemplate.update(sql, params);
				}
			}
		}
	}