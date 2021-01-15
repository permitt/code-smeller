	@Override
	/** {@inheritDoc} */
	public StatementBlock.ReturnStatus_type hasReturn(final CompilationTimeStamp timestamp) {
		if (statementblock != null) {
//			if (StatementBlock.ReturnStatus_type.RS_NO.equals(statementblock.hasReturn(timestamp))) {
//				return StatementBlock.ReturnStatus_type.RS_NO;
//			}
//
//			return StatementBlock.ReturnStatus_type.RS_MAYBE;//it is not know if it will execute even once
			return hasReturn;
		}

		return StatementBlock.ReturnStatus_type.RS_NO;
	}