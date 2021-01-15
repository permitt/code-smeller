	@Override
	public TypeBinding substitute(TypeVariableBinding typeVariable) {
		ReferenceBinding superclass = typeVariable.superclass;
		ReferenceBinding[] superInterfaces = typeVariable.superInterfaces;
		boolean hasSubstituted = false;
		variableLoop: for (int i = 0; i < this.variables.length; i++) {
			InferenceVariable variable = this.variables[i];
			TypeBinding pi = getP(i);
			if (TypeBinding.equalsEquals(pi, typeVariable))
				return variable;
			if (TypeBinding.equalsEquals(pi, superclass)) {
				superclass = variable;
				hasSubstituted = true;
				continue;
			}
			if (superInterfaces != null) {
				int ifcLen = superInterfaces.length; 
				for (int j = 0; j < ifcLen; j++) {
					if (TypeBinding.equalsEquals(pi, superInterfaces[j])) {
						if (superInterfaces == typeVariable.superInterfaces)
							System.arraycopy(superInterfaces, 0, superInterfaces = new ReferenceBinding[ifcLen], 0, ifcLen);
						superInterfaces[j] = variable;
						hasSubstituted = true;
						continue variableLoop;
					}
				}
			}
		}
		if (hasSubstituted) {
			typeVariable = new TypeVariableBinding(typeVariable.sourceName, typeVariable.declaringElement, typeVariable.rank, this.environment);
			typeVariable.superclass = superclass;
			typeVariable.superInterfaces = superInterfaces;
			typeVariable.firstBound = superclass != null ? superclass : superInterfaces[0];
			if (typeVariable.firstBound.hasNullTypeAnnotations())
				typeVariable.tagBits |= TagBits.HasNullTypeAnnotation;
		}
		return typeVariable;
	}