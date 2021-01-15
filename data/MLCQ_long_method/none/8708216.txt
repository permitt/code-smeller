public void setHeight (int height) {
	checkWidget ();
	if (height < 0) return;
	setBounds (0, 0, width, height, false, true);
	if (expanded) parent.layoutItems (parent.indexOf (this) + 1, true);
}