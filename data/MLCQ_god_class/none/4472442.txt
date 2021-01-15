public class FSUtil {
	
	@Deprecated
	public static FSIterator getAnnotationsInSpanIterator(JCas jcas, int type, int beginSpan, int endSpan)
	{
		ConstraintFactory constraintFactory = jcas.getConstraintFactory();
	    FSIntConstraint windowConstraint = constraintFactory.createIntConstraint();
	    windowConstraint.gt(beginSpan-1);
	    windowConstraint.lt(endSpan);
	    
	    Type annotType = jcas.getCasType(type);
	    Feature beginSpanFeature = annotType.getFeatureByBaseName("begin");
	    Feature endSpanFeature = annotType.getFeatureByBaseName("end");
	    
	    FeaturePath beginFeaturePath = jcas.createFeaturePath();
	    beginFeaturePath.addFeature(beginSpanFeature);
	    FSMatchConstraint beginSpanConstraint = constraintFactory.embedConstraint(beginFeaturePath, windowConstraint);
	    
	    FeaturePath endFeaturePath = jcas.createFeaturePath();
	    endFeaturePath.addFeature(endSpanFeature);
	    FSMatchConstraint endSpanConstraint = constraintFactory.embedConstraint(endFeaturePath, windowConstraint);
	    
	    FSMatchConstraint spanConstraint = constraintFactory.and(beginSpanConstraint, endSpanConstraint);
	    
	    JFSIndexRepository indexes = jcas.getJFSIndexRepository();
	    FSIndex<?> annotIndex = indexes.getAnnotationIndex(type);
	    FSIterator<?> annotsInSpanItr = jcas.createFilteredIterator(annotIndex.iterator(), spanConstraint);
	    return annotsInSpanItr;
	}
	
	/**
	 * For correct behavior, requires types to be listed in TypePriorities so that the subiterator works as expected
	 */
	public static FSIterator getAnnotationsIteratorInSpan(JCas jcas, int type, int beginSpan, int endSpan)
	{
	    Annotation ann = new Annotation(jcas, beginSpan, endSpan);
	    ann.addToIndexes();
	    AnnotationIndex<?> annIdx = jcas.getAnnotationIndex(type);
	    FSIterator<?> itr = annIdx.subiterator(ann);
	    ann.removeFromIndexes();
	    return itr;
	}

	/**
	 * Does not use {@link #getAnnotationsInSpan(JCas, int, int, int, int[])} so we don't create a collection
	 * unnecessarily.
	 */
	public static int countAnnotationsInSpan(JCas jcas, int type, int beginSpan, int endSpan, int[] validNeTypes)
	{
	    int count=0;
	    Iterator<?> itr = getAnnotationsIteratorInSpan(jcas, type, beginSpan, endSpan);
	    while(itr.hasNext())
	    {
	    	IdentifiedAnnotation ne = (IdentifiedAnnotation)itr.next();
	    	if(isValidNE(ne.getTypeID(), validNeTypes))
	    		count++;
	    }
	    return count;
	}
	
	private static boolean isValidNE(int currNeType, int[] neTypes)
	{
	    for(int i=0; i<neTypes.length; i++)
		if(currNeType == neTypes[i])
		    return true;
	    
	    return false;
	}
	
	public static List getAnnotationsInSpan(JCas jcas, int type, int beginSpan, int endSpan, int[] validNeTypes)
	{
	    List<IdentifiedAnnotation> list = new ArrayList<IdentifiedAnnotation>();
	    Iterator<?> itr = getAnnotationsIteratorInSpan(jcas, type, beginSpan, endSpan);
	    while(itr.hasNext())
	    {
    		IdentifiedAnnotation ne = (IdentifiedAnnotation)itr.next(); // might be an EventMention or an EntityMention
	    	if(isValidNE(ne.getTypeID(), validNeTypes))
	    		list.add(ne);
	    }
	    return list;
	}

	
	
	/**
	 * returns the number of annotations of specified type in the 
	 */
	public static int countAnnotationsInSpan(JCas jcas, int type, int beginSpan, int endSpan)
	{
	    Annotation ann = new Annotation(jcas, beginSpan, endSpan);
	    ann.addToIndexes();
	    AnnotationIndex<?> annIdx = jcas.getAnnotationIndex(type);
	    ann.removeFromIndexes();
	    return annIdx.size();
	}

	/**
	 * returns a true if the annotation type is present in the span 
	 */
	public static boolean isAnnotationPresentInSpan(JCas jcas, int type, int beginSpan, int endSpan)
	{
	    return (countAnnotationsInSpan(jcas, type, beginSpan, endSpan)>0);
	}	
}