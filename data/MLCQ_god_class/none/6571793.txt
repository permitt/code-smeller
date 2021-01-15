public class ControlTooltipTextProperty extends WidgetStringValueProperty {
	String doGetStringValue(Object source) {
		return ((Control) source).getToolTipText();
	}

	void doSetStringValue(Object source, String value) {
		((Control) source).setToolTipText(value);
	}

	public String toString() {
		return "Control.tooltipText <String>"; //$NON-NLS-1$
	}
}