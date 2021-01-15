	public static BPMNDiagram findBPMNDiagram(final BaseElement baseElement, boolean contains) {
		if (baseElement==null || baseElement.eResource()==null)
			return null;
		ResourceSet resourceSet = baseElement.eResource().getResourceSet();
		if (resourceSet==null)
			return null;
		for (Resource r : resourceSet.getResources()) {
			if (r instanceof Bpmn2Resource) {
				for (EObject o : r.getContents()) {
					if (o instanceof DocumentRoot) {
						DocumentRoot root = (DocumentRoot)o;
						Definitions defs = root.getDefinitions();
						BaseElement bpmnElement;
						for (BPMNDiagram d : defs.getDiagrams()) {
							BPMNDiagram bpmnDiagram = (BPMNDiagram)d;
							bpmnElement = bpmnDiagram.getPlane().getBpmnElement();
							if (bpmnElement == baseElement)
								return bpmnDiagram;
						}
						if (contains) {
							for (BPMNDiagram d : defs.getDiagrams()) {
								BPMNDiagram bpmnDiagram = (BPMNDiagram)d;
								for (DiagramElement de : bpmnDiagram.getPlane().getPlaneElement()) {
									if (de instanceof BPMNShape)
										bpmnElement = ((BPMNShape)de).getBpmnElement();
									else if (de instanceof BPMNEdge)
										bpmnElement = ((BPMNEdge)de).getBpmnElement();
									else
										continue;
									if (bpmnElement == baseElement)
										return bpmnDiagram;
								}
							}
							EObject parent = baseElement.eContainer();
							if (parent instanceof BaseElement && !(parent instanceof Definitions)) {
								BPMNDiagram bpmnDiagram = findBPMNDiagram((BaseElement)parent, true);
								if (bpmnDiagram!=null)
									return bpmnDiagram;
							}
						}
//						for (BPMNDiagram d : defs.getDiagrams()) {
//							BPMNDiagram bpmnDiagram = (BPMNDiagram)d;
//							bpmnElement = bpmnDiagram.getPlane().getBpmnElement();
//							if (bpmnElement instanceof Collaboration) {
//								Collaboration collaboration = (Collaboration)bpmnElement;
//								for (Participant p : collaboration.getParticipants()) {
//									if (baseElement==p)
//										return bpmnDiagram;
//									if (baseElement==p.getProcessRef())
//										return bpmnDiagram;
//								}
//							}
//						}
					}
				}
			}
		}
		return null;
	}