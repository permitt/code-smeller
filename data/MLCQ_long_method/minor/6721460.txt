	public String generateStartTagContent(IDOMElement element) {
		ISourceGenerator generator = element.getModel().getGenerator();
		StringBuffer buffer = new StringBuffer();

		buffer.append(' ');
		String tagName = generator.generateTagName(element);
		if (tagName != null) {
			buffer.append(tagName);
		}

		NamedNodeMap attributes = element.getAttributes();
		int length = attributes.getLength();
		for (int i = 0; i < length; i++) {
			Attr attr = (Attr) attributes.item(i);
			if (attr == null) {
				continue;
			}
			buffer.append(' ');
			String attrName = generator.generateAttrName(attr);
			if (attrName != null) {
				buffer.append(attrName);
			}
			String attrValue = generator.generateAttrValue(attr);
			if (attrValue != null) {
				// attr name only for HTML boolean and JSP
				buffer.append('=');
				buffer.append(attrValue);
			}
		}

		buffer.append(' ');

		return buffer.toString();
	}