		@Override
		public Object visit(AnnotationPointcut node, Object data) {
			hasDynamicContent = true;
			return null;
		}