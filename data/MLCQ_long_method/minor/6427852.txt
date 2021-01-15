	public static Point computeWrapSize(GC gc, String text, int wHint) {
		BreakIterator wb = BreakIterator.getWordInstance();
		wb.setText(text);
		FontMetrics fm = gc.getFontMetrics();
		int lineHeight = fm.getHeight();

		int saved = 0;
		int last = 0;
		int height = lineHeight;
		int maxWidth = 0;
		for (int loc = wb.first(); loc != BreakIterator.DONE; loc = wb.next()) {
			String word = text.substring(saved, loc);
			Point extent = gc.textExtent(word);
			if (extent.x > wHint) {
				// overflow
				saved = last;
				height += extent.y;
				// switch to current word so maxWidth will accommodate very long single words
				word = text.substring(last, loc);
				extent = gc.textExtent(word);
			}
			maxWidth = Math.max(maxWidth, extent.x);
			last = loc;
		}
		/*
		 * Correct the height attribute in case it was calculated wrong due to wHint being less than maxWidth.
		 * The recursive call proved to be the only thing that worked in all cases. Some attempts can be made
		 * to estimate the height, but the algorithm needs to be run again to be sure.
		 */
		if (maxWidth > wHint)
			return computeWrapSize(gc, text, maxWidth);
		return new Point(maxWidth, height);
	}