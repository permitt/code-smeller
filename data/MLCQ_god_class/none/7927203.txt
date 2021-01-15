public class RotateLaneFeature extends AbstractRotateContainerFeature {

	/**
	 * @param fp
	 */
	public RotateLaneFeature(IFeatureProvider fp) {
		super(fp);
	}
	
	@Override
	public String getName() {
	    return Messages.RotateLaneFeature_Name;
	}
	
	@Override
	public String getDescription() {
	    return Messages.RotateLaneFeature_Description;
	}
}