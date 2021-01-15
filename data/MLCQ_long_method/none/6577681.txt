  public void setShowFocusedControl( boolean show ) {
    checkWidget();
    if( showFocusedControl != show ) {
      showFocusedControl = show;
      if( showFocusedControl ) {
        Control control = getDisplay().getFocusControl();
        if( contains( control ) ) {
          showControl( control );
        }
      }
    }
  }