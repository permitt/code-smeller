	public TypeBinding createBinding(MethodScope scope, TypeBinding typeBinding) {
		if (this.binding == null) {
			// for default constructors and fake implementation of abstract methods 
			this.binding = new LocalVariableBinding(this, typeBinding, this.modifiers, scope);
		} else if (!this.binding.type.isValidBinding()) {
			AbstractMethodDeclaration methodDecl = scope.referenceMethod();
			if (methodDecl != null) {
				MethodBinding methodBinding = methodDecl.binding;
				if (methodBinding != null) {
					methodBinding.tagBits |= TagBits.HasUnresolvedArguments;
				}
			}
		}
		if ((this.binding.tagBits & TagBits.AnnotationResolved) == 0) {
			resolveAnnotations(scope, this.annotations, this.binding, true);
			if (scope.compilerOptions().sourceLevel >= ClassFileConstants.JDK1_8) {
				Annotation.isTypeUseCompatible(this.type, scope, this.annotations);
				scope.validateNullAnnotation(this.binding.tagBits, this.type, this.annotations);
			}
		}
		this.binding.declaration = this;
		return this.binding.type; // might have been updated during resolveAnnotations (for typeAnnotations)
	}