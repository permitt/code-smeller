void gtk_widget_set_align(long /*int*/ widget, int hAlign, int vAlign) {
	GTK.gtk_widget_set_halign (widget, hAlign);
	GTK.gtk_widget_set_valign (widget, vAlign);
}