	public String unparse() {
		StringBuffer text = new StringBuffer(100);
		if (getPublicID() == null || getPublicID().equals("")) { //$NON-NLS-1$
			text.append("SYSTEM "); //$NON-NLS-1$
		}
		else {
			text.append("PUBLIC \"").append(getPublicID()).append("\" "); //$NON-NLS-1$ //$NON-NLS-2$
		}
		String systemId = getSystemID();

		text.append("\"").append(systemId).append("\""); //$NON-NLS-1$ //$NON-NLS-2$

		DTDNotation notation = getNotation();
		if (notation != null)
			text.append(" NDATA ").append(notation.getName()); //$NON-NLS-1$

		return text.toString();
	}