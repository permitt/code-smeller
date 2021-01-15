public class CreateTextAnnotationFeature extends AbstractCreateArtifactFeature<TextAnnotation> {

	public CreateTextAnnotationFeature(IFeatureProvider fp) {
		super(fp);
	}

	@Override
	public boolean canCreate(ICreateContext context) {
		return FeatureSupport.isValidArtifactTarget(context);
	}

	@Override
	public Object[] create(ICreateContext context) {

		TextAnnotation ta = createBusinessObject(context);
		PictogramElement pe = addGraphicalRepresentation(context, ta);

		return new Object[] { ta, pe };
	}

	@Override
	protected String getStencilImageId() {
		return ImageProvider.IMG_16_TEXT_ANNOTATION;
	}

	@Override
	public String getCreateImageId() {
		return ImageProvider.IMG_16_TEXT_ANNOTATION;
	}

	@Override
	public String getCreateLargeImageId() {
		return getCreateImageId(); // FIXME
	}

	/* (non-Javadoc)
	 * @see org.eclipse.bpmn2.modeler.core.features.AbstractBpmn2CreateFeature#getBusinessObjectClass()
	 */
	@Override
	public EClass getBusinessObjectClass() {
		return Bpmn2Package.eINSTANCE.getTextAnnotation();
	}
}