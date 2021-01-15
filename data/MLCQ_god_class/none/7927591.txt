	class BPMN2ResourceVisitor implements IResourceVisitor {
		IProgressMonitor monitor;

		public BPMN2ResourceVisitor(IProgressMonitor monitor) {
			this.monitor = monitor;
		}

		public boolean visit(IResource resource) {
			// checkXML(resource);
			validate(resource, monitor);
			// return true to continue visiting children.
			return true;
		}
	}