@Override
public String toString() {
	StringBuilder buffer = new StringBuilder("["); //$NON-NLS-1$
	for (int i = 0; i < this.size; i++) {
		buffer.append("\n"); //$NON-NLS-1$
		buffer.append(this.elements[i]);
	}
	buffer.append("\n]"); //$NON-NLS-1$
	return buffer.toString();
}