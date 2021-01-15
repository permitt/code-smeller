		@Override
		public IInformationControl createInformationControl(Shell parent) {
			return new AnnotationExpansionControl(parent, SWT.NONE,
					fAnnotationAccess);
		}