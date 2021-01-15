	@Override
	public boolean visit(TryStatement node) {
		this.result.append("try "); //$NON-NLS-1$
		int level = node.getAST().apiLevel();
		if (level >= JLS4_INTERNAL) {
			StructuralPropertyDescriptor desc = level < JLS9_INTERNAL ? INTERNAL_TRY_STATEMENT_RESOURCES_PROPERTY : TryStatement.RESOURCES2_PROPERTY;
			visitList(node, desc, String.valueOf(';'), String.valueOf('('), String.valueOf(')'));
		}
		getChildNode(node, TryStatement.BODY_PROPERTY).accept(this);
		this.result.append(' ');
		visitList(node, TryStatement.CATCH_CLAUSES_PROPERTY, null);
		ASTNode finallyClause= getChildNode(node, TryStatement.FINALLY_PROPERTY);
		if (finallyClause != null) {
			this.result.append(" finally "); //$NON-NLS-1$
			finallyClause.accept(this);
		}
		return false;
	}