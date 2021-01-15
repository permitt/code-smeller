public void testBug330313_wksp1_15_njl() {
	this.formatterPrefs.join_wrapped_lines = false;
	setPageWidth80();
	String source =
		"package wksp1;\n" + 
		"\n" + 
		"public class X15 {\n" + 
		"	public void foo() {\n" + 
		"		if (true) {\n" + 
		"			if (fieldBinding.declaringClass != this.actualReceiverType\n" + 
		"				&& !this.actualReceiverType.isArrayType()	\n" + 
		"				&& fieldBinding.declaringClass != null\n" + 
		"				&& fieldBinding.constant == NotAConstant\n" + 
		"				&& ((currentScope.environment().options.targetJDK >= ClassFileConstants.JDK1_2 \n" + 
		"						&& !fieldBinding.isStatic()\n" + 
		"						&& fieldBinding.declaringClass.id != T_Object) // no change for Object fields (if there was any)\n" + 
		"					|| !fieldBinding.declaringClass.canBeSeenBy(currentScope))){\n" + 
		"				this.codegenBinding = currentScope.enclosingSourceType().getUpdatedFieldBinding(fieldBinding, (ReferenceBinding)this.actualReceiverType);\n" + 
		"			}\n" + 
		"		}\n" + 
		"	}\n" + 
		"}\n";
	formatSource(source,
		"package wksp1;\n" + 
		"\n" + 
		"public class X15 {\n" + 
		"	public void foo() {\n" + 
		"		if (true) {\n" + 
		"			if (fieldBinding.declaringClass != this.actualReceiverType\n" + 
		"					&& !this.actualReceiverType.isArrayType()\n" + 
		"					&& fieldBinding.declaringClass != null\n" + 
		"					&& fieldBinding.constant == NotAConstant\n" + 
		"					&& ((currentScope\n" + 
		"							.environment().options.targetJDK >= ClassFileConstants.JDK1_2\n" + 
		"							&& !fieldBinding.isStatic()\n" + 
		"							&& fieldBinding.declaringClass.id != T_Object) // no\n" + 
		"																			// change\n" + 
		"																			// for\n" + 
		"																			// Object\n" + 
		"																			// fields\n" + 
		"																			// (if\n" + 
		"																			// there\n" + 
		"																			// was\n" + 
		"																			// any)\n" + 
		"							|| !fieldBinding.declaringClass\n" + 
		"									.canBeSeenBy(currentScope))) {\n" + 
		"				this.codegenBinding = currentScope.enclosingSourceType()\n" + 
		"						.getUpdatedFieldBinding(fieldBinding,\n" + 
		"								(ReferenceBinding) this.actualReceiverType);\n" + 
		"			}\n" + 
		"		}\n" + 
		"	}\n" + 
		"}\n"
	);
}