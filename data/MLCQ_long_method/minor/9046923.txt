public void testBug427626() {
	runNegativeTest(
		new String[] {
			"X.java",
			"import java.util.Arrays;\n" + 
			"import java.util.List;\n" + 
			"\n" + 
			"public class X {\n" + 
			"	void m() {\n" + 
			"        List<String> ss = Arrays.asList(\"1\", \"2\", \"3\");\n" + 
			"        \n" + 
			"        ss.stream().map(s -> {\n" + 
			"          class L1 {};\n" + 
			"          class L2 {\n" + 
			"            void mm(L1 l) {}\n" + 
			"          }\n" + 
			"          return new L2().mm(new L1());\n" + 
			"        }).forEach(e -> System.out.println(e));\n" + 
			"	}\n" + 
			"}"
		},
		// 8u20 emits just one message inferred type not conforming to upper bound.
		"----------\n" + 
		"1. ERROR in X.java (at line 8)\n" +
		"	ss.stream().map(s -> {\n" +
		"          class L1 {};\n" +
		"          class L2 {\n" +
		"            void mm(L1 l) {}\n" +
		"          }\n" +
		"          return new L2().mm(new L1());\n" +
		"        }).forEach(e -> System.out.println(e));\n" +
		"	^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n" +
		"Cannot infer type argument(s) for <R> map(Function<? super T,? extends R>)\n" +
		"----------\n" +
		"2. ERROR in X.java (at line 13)\n" + 
		"	return new L2().mm(new L1());\n" + 
		"	^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n" + 
		"Cannot return a void result\n" + 
		"----------\n");
}