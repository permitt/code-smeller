  public void setLocation( int x, int y ) {
    checkWidget();
    if( ( style & ( SWT.BAR | SWT.DROP_DOWN ) ) == 0 ) {
      this.x = x;
      this.y = y;
      hasLocation = true;
    }
  }