public interface IExternalSchemaLocationProvider {
	String SCHEMA_LOCATION = "http://apache.org/xml/properties/schema/external-schemaLocation"; //$NON-NLS-1$
	String NO_NAMESPACE_SCHEMA_LOCATION = "http://apache.org/xml/properties/schema/external-noNamespaceSchemaLocation"; //$NON-NLS-1$

	/**
	 * Provided the file path URI, this will return the external schema location. The schema location is associated to a specific property,
	 * which serves as the key in the map. The supported properties are:
	 * 
	 * <p><b>http://apache.org/xml/properties/schema/external-schemaLocation</b> - The value for this property follows the same rules
	 * as the schemaLocation attribute for an XML document (i.e., multiple schemas are acceptable and must be white-space separated).</p>
	 * 
	 * <p><b>http://apache.org/xml/properties/schema/external-noNamespaceSchemaLocation</b> - The value for this property follows the same
	 * rules as the noNamespaceSchemaLocation attribute for an XML document (i.e., only one schema is allowed).
	 * 
	 * @param filePath the path for the XML file
	 * @return a {@link Map} associating the external-schemaLocation and/or external-noNamespaceSchemaLocation to the schema location
	 */
	Map getExternalSchemaLocation(URI fileURI);
}