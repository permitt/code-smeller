int readBlock() {
	int size = -1;
	try {
		size = inputStream.read();
		if (size == -1) {
			SWT.error(SWT.ERROR_INVALID_IMAGE);
		}
		block[0] = (byte)size;
		size = inputStream.read(block, 1, size);
		if (size == -1) {
			SWT.error(SWT.ERROR_INVALID_IMAGE);
		}
	} catch (Exception e) {
		SWT.error(SWT.ERROR_IO, e);
	}
	return size;
}