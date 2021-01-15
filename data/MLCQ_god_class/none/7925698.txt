public class EventSelectionBehavior {

	public static boolean canApplyTo(PictogramElement element) {
		if (element.getLink() == null || !(element instanceof ContainerShape)) {
			return false;
		}

		EList<EObject> objects = element.getLink().getBusinessObjects();

		for (EObject eObject : objects) {
			if (eObject instanceof Event && !(eObject instanceof BoundaryEvent)) {
				return true;
			}
		}

		return false;
	}

	public static GraphicsAlgorithm[] getClickArea(PictogramElement element) {
		Collection<PictogramElement> children = Graphiti.getPeService().getPictogramElementChildren(element);
		PictogramElement first = children.iterator().next();
		return new GraphicsAlgorithm[] { first.getGraphicsAlgorithm() };
	}

	public static GraphicsAlgorithm getSelectionBorder(PictogramElement element) {
		Collection<Shape> children = Graphiti.getPeService().getAllContainedShapes((ContainerShape) element);
		PictogramElement first = children.iterator().next();
		return first.getGraphicsAlgorithm();
	}
}