public class CSSValueListImpl extends AbstractCSSNode implements CSSValueList {

	List<CSSValue> values;

	public CSSValueListImpl(LexicalUnit parsePropertyValue) {
		values = new ArrayList<>();

		LexicalUnit unit = parsePropertyValue;
		while(unit != null) {
			values.add(CSSValueFactory.newPrimitiveValue(unit));
			unit = unit.getNextLexicalUnit();
		}
	}

	@Override
	public int getLength() {
		return values.size();
	}

	@Override
	public CSSValue item(int index) {
		return values.get(index);
	}

	@Override
	public String getCssText() {
		StringBuilder buffer = new StringBuilder();
		for (CSSValue value : values) {
			buffer.append(value.getCssText());
			buffer.append(" ");
		}
		return buffer.toString().trim();
	}

	@Override
	public short getCssValueType() {
		return CSS_VALUE_LIST;
	}

	@Override
	public void setCssText(String arg0) throws DOMException {
		throw new UnsupportedOperationException("NOT YET IMPLEMENTED");
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		for (CSSValue cssValue : values) {
			sb.append(cssValue.getCssText() + "\n");
		}
		return sb.toString();
	}

}