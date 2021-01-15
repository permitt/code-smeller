	@Override
	public void configure(Binder binder) {
		properties = tryBindProperties(binder, "org/eclipse/xtext/grammarinheritance/BaseInheritanceTestLanguage.properties");
		super.configure(binder);
	}