void headerHideToolTip() {
	if (toolTipShell == null) return;
	for (int toolTipEvent : toolTipEvents) {
		header.removeListener (toolTipEvent, toolTipListener);
	}
	toolTipShell.dispose ();
	toolTipShell = null;
	toolTipLabel = null;
}