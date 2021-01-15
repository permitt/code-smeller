		@Override
		public String getText(Object element) {
			if (element instanceof GrailsProjectStructureTypes) {
				return ((GrailsProjectStructureTypes) element).getDisplayName();
			} else if (element instanceof String) {
				return (String)element;
			}
			return ""+element;
		}