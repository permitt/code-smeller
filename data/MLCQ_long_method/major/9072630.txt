	public boolean condition18_5_2_bullet_3_3_1(InferenceVariable alpha, TypeBinding targetType) {
		// T is a reference type, but is not a wildcard-parameterized type, and either 
		// i) B2 contains a bound of one of the forms  = S or S <: , where S is a wildcard-parameterized type, or ...
		if (targetType.isBaseType()) return false;
		if (InferenceContext18.parameterizedWithWildcard(targetType) != null) return false;
		ThreeSets ts = this.boundsPerVariable.get(alpha.prototype());
		if (ts == null)
			return false;
		if (ts.sameBounds != null) {
			Iterator<TypeBound> bounds = ts.sameBounds.iterator();
			while (bounds.hasNext()) {
				TypeBound bound = bounds.next();
				if (InferenceContext18.parameterizedWithWildcard(bound.right) != null)
					return true;
			}
		}
		if (ts.superBounds != null) {
			Iterator<TypeBound> bounds = ts.superBounds.iterator();
			while (bounds.hasNext()) {
				TypeBound bound = bounds.next();
				if (InferenceContext18.parameterizedWithWildcard(bound.right) != null)
					return true;
			}
		}
		// ii) B2 contains two bounds of the forms S1 <:  and S2 <: , where
		//     S1 and S2 have supertypes (4.10) that are two different parameterizations of the same generic class or interface.
		if (ts.superBounds != null) {
			ArrayList<TypeBound> superBounds = new ArrayList<>(ts.superBounds);
			int len = superBounds.size();
			for (int i=0; i<len; i++) {
				TypeBinding s1 = superBounds.get(i).right;
				for (int j=i+1; j<len; j++) {
					TypeBinding s2 = superBounds.get(j).right;
					TypeBinding[] supers = superTypesWithCommonGenericType(s1, s2);
					if (supers != null) {
						/* HashMap<K#8,V#9> and HashMap<K#8,ArrayList<T>> with an instantiation for V9 = ArrayList<T> already in the 
						   bound set should not be seen as two different parameterizations of the same generic class or interface.
						   See https://bugs.eclipse.org/bugs/show_bug.cgi?id=432626 for a test that triggers this condition.
						   See https://bugs.openjdk.java.net/browse/JDK-8056092: recommendation is to check for proper types.
						*/
						if (supers[0].isProperType(true) && supers[1].isProperType(true) && !TypeBinding.equalsEquals(supers[0], supers[1]))
							return true;
					}
				}
			}
		}
		return false;
	}