	public SWTFocusCellManager(ColumnViewer viewer,
			FocusCellHighlighter focusDrawingDelegate,
			CellNavigationStrategy navigationDelegate) {
		this.viewer = viewer;
		this.cellHighlighter = focusDrawingDelegate;
		if( this.cellHighlighter != null ) {
			this.cellHighlighter.setMgr(this);
		}

		this.navigationStrategy = navigationDelegate;
		hookListener(viewer);
	}