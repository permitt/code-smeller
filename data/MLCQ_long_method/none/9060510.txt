	public void test005() throws Exception {
		this.runConformTest(
			new String[] {
				"X.java",
				"import java.lang.annotation.*;\n" +
				"import java.util.List;\n" +
				"import static java.lang.annotation.ElementType.*; \n" +
				"@Target(TYPE_USE)\n" +
				"@interface Critical {}\n" +
				"@Target(TYPE_USE)\n" +
				"@interface NonEmpty {}\n" +
				"@Target(TYPE_USE)\n" +
				"@interface Readonly {}\n" +
				"class TemperatureException extends RuntimeException{}\n" +
				"class X {\n" +
				"	void monitorTemperature() throws @Critical TemperatureException {}\n" +
				"}\n",
		},
		"");
		String expectedOutput =
				"    RuntimeInvisibleTypeAnnotations: \n" + 
				"      #19 @Critical(\n" + 
				"        target type = 0x17 THROWS\n" + 
				"        throws index = 0\n" + 
				"      )\n";
		checkDisassembledClassFile(OUTPUT_DIR + File.separator + "X.class", "X", expectedOutput, ClassFileBytesDisassembler.SYSTEM);
	}