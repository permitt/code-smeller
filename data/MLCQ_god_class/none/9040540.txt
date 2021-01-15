public class GenericFactory extends BaseFactory {
	public static AbstractGenericProcessor PROCESSOR;
	public static AnnotationProcessor fact;
	
	public static void setProcessor(AbstractGenericProcessor p) {
		PROCESSOR = p;
	}

	public GenericFactory() {
		super(GenericAnnotation.class.getName());
	}

	public AnnotationProcessor getProcessorFor(Set<AnnotationTypeDeclaration> arg0, AnnotationProcessorEnvironment env) {
		PROCESSOR.setEnv(env);
		return PROCESSOR;
	}

}