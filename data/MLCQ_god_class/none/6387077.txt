public interface ICSSPropertyPaddingHandler extends ICSSPropertyHandler {

	/**
	 * A shorthand property for setting all four paddings in one declaration.
	 * Available values are
	 * {padding-top, padding-right, padding-bottom, padding-left}
	 * @param element
	 * @param value
	 * @param pseudo
	 * @param engine
	 * @throws Exception
	 */
	//TODO support in future values {inherit}
	public void applyCSSPropertyPadding(Object element, CSSValue value,
			String pseudo, CSSEngine engine) throws Exception;

	/**
	 * Sets the top padding. Available values are {length}
	 *
	 * @param element
	 * @param value
	 * @param pseudo
	 * @param engine
	 * @throws Exception
	 */
	//TODO support in future values {auto, %, inherit}
	public void applyCSSPropertyPaddingTop(Object element,
			CSSValue value, String pseudo, CSSEngine engine) throws Exception;


	/**
	 * Sets the right padding. Available values are {length}
	 *
	 * @param element
	 * @param value
	 * @param pseudo
	 * @param engine
	 * @throws Exception
	 */
	//TODO support in future values {auto, %, inherit}
	public void applyCSSPropertyPaddingRight(Object element,
			CSSValue value, String pseudo, CSSEngine engine) throws Exception;


	/**
	 * Sets the bottom padding. Available values are {length}
	 *
	 * @param element
	 * @param value
	 * @param pseudo
	 * @param engine
	 * @throws Exception
	 */
	//TODO support in future values {auto, %, inherit}
	public void applyCSSPropertyPaddingBottom(Object element,
			CSSValue value, String pseudo, CSSEngine engine) throws Exception;


	/**
	 * Sets the left padding. Available values are {length}
	 *
	 * @param element
	 * @param value
	 * @param pseudo
	 * @param engine
	 * @throws Exception
	 */
	//TODO support in future values {auto, %, inherit}
	public void applyCSSPropertyPaddingLeft(Object element, CSSValue value,
			String pseudo, CSSEngine engine) throws Exception;


	public String retrieveCSSPropertyPadding(Object element, String pseudo,
			CSSEngine engine) throws Exception;

	public String retrieveCSSPropertyPaddingTop(Object element,
			String pseudo, CSSEngine engine) throws Exception;

	public String retrieveCSSPropertyPaddingRight(Object element,
			String pseudo, CSSEngine engine) throws Exception;

	public String retrieveCSSPropertyPaddingBottom(Object element,
			String pseudo, CSSEngine engine) throws Exception;

	public String retrieveCSSPropertyPaddingLeft(Object element,
			String pseudo, CSSEngine engine) throws Exception;

}