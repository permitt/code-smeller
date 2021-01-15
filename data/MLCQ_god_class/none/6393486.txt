/* package */class VisualTextDirectionSegmentListener implements SegmentListener {

	private String textDirection;

	/**
	 * Creates a new segment listener that enforces Visual Text Direction
	 * support.
	 *
	 * @param textDir
	 *            the text direction Possible values are:
	 *            <ul>
	 *            <li> {@link BidiUtils#VISUAL_LEFT_TO_RIGHT}
	 *            <li> {@link BidiUtils#VISUAL_RIGHT_TO_LEFT}
	 *            </ul>
	 */
	public VisualTextDirectionSegmentListener(String textDir) {
		textDirection = textDir;
	}

	@Override
	public void getSegments(SegmentEvent event) {
		int length = event.lineText.length();
		if (length > 0) {
			event.segments = new int[2];
			event.segments[0] = 0;
			event.segments[1] = length;
			event.segmentsChars = new char[2];
			event.segmentsChars[0] = BidiUtils.VISUAL_RIGHT_TO_LEFT.equals(textDirection)
					? BidiUtils.RLO
					: BidiUtils.LRO;
			event.segmentsChars[1] = BidiUtils.PDF;
		}
	}
}