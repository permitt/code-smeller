public class ReadmeMarkerResolutionGenerator implements
        IMarkerResolutionGenerator2 {

    @Override
	public IMarkerResolution[] getResolutions(IMarker marker) {
        return new IMarkerResolution[] { new AddSentenceResolution() };
    }

    @Override
	public boolean hasResolutions(IMarker marker) {
        return true;
    }

}