		@Override
		public boolean visit(IModelElement element) {
			if (type == null) {
				if (element.getElementType() == IModelElement.TYPE
						&& simpleTypeName.equals(element.getElementName())) {
					type = (IType) element;
					return false;
				}
				return true;
			} else {
				return false;
			}
		}