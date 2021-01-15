@Override
protected IBinaryType createInfoFromClassFileInJar(Openable classFile) {
	String filePath = (((ClassFile)classFile).getType().getFullyQualifiedName('$')).replace('.', '/') + SuffixConstants.SUFFIX_STRING_class;
	IPackageFragmentRoot root = classFile.getPackageFragmentRoot();
	IPath path = root.getPath();
	// take the OS path for external jars, and the forward slash path for internal jars
	String rootPath = path.getDevice() == null ? path.toString() : path.toOSString();
	String documentPath = rootPath + IJavaSearchScope.JAR_FILE_ENTRY_SEPARATOR + filePath;
	IBinaryType binaryType = (IBinaryType)this.binariesFromIndexMatches.get(documentPath);
	if (binaryType != null) {
		this.infoToHandle.put(binaryType, classFile);
		return binaryType;
	} else {
		return super.createInfoFromClassFileInJar(classFile);
	}
}