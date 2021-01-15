static class MethodHolder extends AnnotationHolder {
	AnnotationBinding[][] parameterAnnotations; // is null if empty

MethodHolder(AnnotationBinding[] annotations, AnnotationBinding[][] parameterAnnotations) {
	super();
	setAnnotations(annotations);
	this.parameterAnnotations = parameterAnnotations;
}
@Override
public AnnotationBinding[][] getParameterAnnotations() {
	return this.parameterAnnotations;
}
@Override
AnnotationBinding[] getParameterAnnotations(int paramIndex) {
	AnnotationBinding[] result = this.parameterAnnotations == null ? null : this.parameterAnnotations[paramIndex];
	return result == null ? Binding.NO_ANNOTATIONS : result;
}
@Override
AnnotationHolder setAnnotations(AnnotationBinding[] annotations) {
	this.annotations = annotations == null || annotations.length == 0 ? Binding.NO_ANNOTATIONS : annotations;
	return this;
}
}