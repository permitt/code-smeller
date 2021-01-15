public interface IClassFileAttribute {

	/**
	 * Answer back the attribute name index in the constant pool as specified
	 * in the JVM specifications.
	 *
	 * @return the attribute name index in the constant pool
	 */
	int getAttributeNameIndex();

	/**
	 * Answer back the attribute name as specified
	 * in the JVM specifications.
	 *
	 * @return the attribute name
	 */
	char[] getAttributeName();

	/**
	 * Answer back the attribute length as specified
	 * in the JVM specifications.
	 *
	 * @return the attribute length
	 */
	long getAttributeLength();
}