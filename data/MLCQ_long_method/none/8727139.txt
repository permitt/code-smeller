void setLineJustify(int startLine, int count, boolean justify) {
	if (lines == null) lines = new LineInfo[lineCount];
	for (int i = startLine; i < startLine + count; i++) {
		if (lines[i] == null) {
			lines[i] = new LineInfo();
		}
		lines[i].flags |= JUSTIFY;
		lines[i].justify = justify;
	}
}