public Cursor(Device device, int style) {
	super(device);
	NSAutoreleasePool pool = null;
	if (!NSThread.isMainThread()) pool = (NSAutoreleasePool) new NSAutoreleasePool().alloc().init();
	boolean shouldCreateCursor = false;
	try {
		switch (style) {
			case SWT.CURSOR_HAND:			handle = NSCursor.pointingHandCursor(); break;
			case SWT.CURSOR_ARROW:			handle = NSCursor.arrowCursor(); break;
			case SWT.CURSOR_WAIT:			{
												handle = busyButClickableCursor();
												if (handle == null) shouldCreateCursor = true; // create when handle was not retrieved
												break;
											}
			case SWT.CURSOR_CROSS:			handle = NSCursor.crosshairCursor(); break;
			case SWT.CURSOR_APPSTARTING:		handle = NSCursor.arrowCursor(); break;
			case SWT.CURSOR_HELP:			handle = NSCursor.crosshairCursor(); break;
			case SWT.CURSOR_SIZEALL:			handle = NSCursor.crosshairCursor(); break;
			case SWT.CURSOR_SIZENESW:		handle = NSCursor.crosshairCursor(); break;
			case SWT.CURSOR_SIZENS:			handle = NSCursor.resizeUpDownCursor(); break;
			case SWT.CURSOR_SIZENWSE:		handle = NSCursor.crosshairCursor(); break;
			case SWT.CURSOR_SIZEWE:			handle = NSCursor.resizeLeftRightCursor(); break;
			case SWT.CURSOR_SIZEN:			handle = NSCursor.resizeUpCursor(); break;
			case SWT.CURSOR_SIZES:			handle = NSCursor.resizeDownCursor(); break;
			case SWT.CURSOR_SIZEE:			handle = NSCursor.resizeRightCursor(); break;
			case SWT.CURSOR_SIZEW:			handle = NSCursor.resizeLeftCursor(); break;
			case SWT.CURSOR_SIZENE:			handle = NSCursor.crosshairCursor(); break;
			case SWT.CURSOR_SIZESE:			handle = NSCursor.crosshairCursor(); break;
			case SWT.CURSOR_SIZESW:			handle = NSCursor.crosshairCursor(); break;
			case SWT.CURSOR_SIZENW:			handle = NSCursor.crosshairCursor(); break;
			case SWT.CURSOR_UPARROW:			handle = NSCursor.crosshairCursor(); break;
			case SWT.CURSOR_IBEAM:			shouldCreateCursor = true; break;
			case SWT.CURSOR_NO:				handle = NSCursor.operationNotAllowedCursor(); break;
			default:
				SWT.error(SWT.ERROR_INVALID_ARGUMENT);
		}
		if (handle == null && shouldCreateCursor) {
			NSImage nsImage = (NSImage)new NSImage().alloc();
			NSBitmapImageRep nsImageRep = (NSBitmapImageRep)new NSBitmapImageRep().alloc();
			handle = (NSCursor)new NSCursor().alloc();
			int width = 16, height = 16;
			NSSize size = new NSSize();
			size.width = width;
			size.height =  height;
			nsImage = nsImage.initWithSize(size);
			nsImageRep = nsImageRep.initWithBitmapDataPlanes(0, width, height, 8, 4, true, false, OS.NSDeviceRGBColorSpace,
					OS.NSAlphaFirstBitmapFormat | OS.NSAlphaNonpremultipliedBitmapFormat, width*4, 32);
			NSPoint point = new NSPoint();
			if (style == SWT.CURSOR_WAIT) {
				C.memmove(nsImageRep.bitmapData(), WAIT_SOURCE, WAIT_SOURCE.length);
			} else { //style == SWT.CURSOR_IBEAM
				C.memmove(nsImageRep.bitmapData(), SHADOWED_IBEAM_SOURCE, SHADOWED_IBEAM_SOURCE.length);
				point.x = 4; point.y = 8;			// values from NSCursor.IBeamCursor().hotSpot();
			}
			nsImage.addRepresentation(nsImageRep);
			handle = handle.initWithImage(nsImage, point);
			nsImageRep.release();
			nsImage.release();
		} else {
			handle.retain();
		}
		handle.setOnMouseEntered(true);
		init();
	} finally {
		if (pool != null) pool.release();
	}
}