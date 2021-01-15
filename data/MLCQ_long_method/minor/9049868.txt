public void testFormatDefaultBigFile() {
	tagAsSummary("Format big file with default options", false); // do NOT put in fingerprint yet...

	// Warm up
	String source = FORMAT_TYPE_SOURCE;
	int warmup = WARMUP_COUNT;
	for (int i=0; i<warmup; i++) {
		long start = System.currentTimeMillis();
		new DefaultCodeFormatter().format(CodeFormatter.K_COMPILATION_UNIT, source, 0, source.length(), 0, null);
		if (i==0) {
			System.out.println("	Time to format big file ("+source.length()+" chars) = "+(System.currentTimeMillis()-start)+"ms");
		}
	}

	// Measures
	resetCounters();
	int measures = MEASURES_COUNT;
	for (int i=0; i<measures; i++) {
		runGc();
		startMeasuring();
		new DefaultCodeFormatter().format(CodeFormatter.K_COMPILATION_UNIT, source, 0, source.length(), 0, null);
		stopMeasuring();
	}

	// Commit
	commitMeasurements();
	assertPerformance();
}