public class BusyIndicator extends Canvas {
	protected Image[] images = new Image[13];
	protected Image image;

	protected Thread busyThread;
	protected boolean stop;

	private static final String URL_BUSY = "$nl$/icons/obj16/busy/"; //$NON-NLS-1$

	/**
	 * BusyWidget constructor comment.
	 * @param parent org.eclipse.swt.widgets.Composite
	 * @param style int
	 */
	public BusyIndicator(Composite parent, int style) {
		super(parent, style);

		ImageResourceManager imageManager = new ImageResourceManager(this);

		for (int i = 0; i < 13; i++) {
			ImageDescriptor id = ImageResourceManager.
					getImageDescriptor(URL_BUSY + (i + 1) + ".gif"); //$NON-NLS-1$

			images[i] = imageManager.getImage(id);
		}

		addPaintListener(event -> onPaint(event));

		image = images[0];
	}

	@Override
	public Point computeSize(int wHint, int hHint, boolean changed) {
		return new Point(25, 25);
	}

	/**
	 * Creates a thread to animate the image.
	 */
	protected synchronized void createBusyThread() {
		if (busyThread != null)
			return;

		stop = false;
		busyThread = new Thread() {
			protected int count;
			@Override
			public void run() {
				try {
					count = 1;
					while (!stop) {
						Display.getDefault().syncExec(() -> {
							if (!stop) {
								if (count < 13)
									setImage(images[count]);
								count++;
								if (count > 12)
									count = 1;
							}
						});
						try {
							sleep(125);
						} catch (Exception e) {
							// ignore
						}
					}
					if (busyThread == null)
						Display.getDefault().syncExec(new Thread() {
							@Override
							public void run() {
								setImage(images[0]);
							}
						});
				} catch (Exception e) {
					Trace.trace(Trace.WARNING, "Busy error", e); //$NON-NLS-1$
				}
			}
		};

		busyThread.setPriority(Thread.NORM_PRIORITY + 2);
		busyThread.setDaemon(true);
		busyThread.start();
	}

	@Override
	public void dispose() {
		stop = true;
		busyThread = null;
		super.dispose();
	}

	/**
	 * Return the image or <code>null</code>.
	 */
	public Image getImage() {
		return image;
	}

	/**
	 * Returns true if it is currently busy.
	 *
	 * @return boolean
	 */
	public boolean isBusy() {
		return (busyThread != null);
	}

	/*
	 * Process the paint event
	 */
	protected void onPaint(PaintEvent event) {
		Rectangle rect = getClientArea();
		if (rect.width == 0 || rect.height == 0)
			return;

		GC gc = event.gc;
		if (image != null)
			gc.drawImage(image, 2, 2);
	}

	/**
	 * Sets the indicators busy count up (true) or down (false) one.
	 *
	 * @param busy boolean
	 */
	public synchronized void setBusy(boolean busy) {
		if (busy) {
			if (busyThread == null)
				createBusyThread();
		} else {
			if (busyThread != null) {
				stop = true;
				busyThread = null;
			}
		}
	}

	/**
	 * Set the image.
	 * The value <code>null</code> clears it.
	 */
	public void setImage(Image image) {
		if (image != this.image && !isDisposed()) {
			this.image = image;
			redraw();
		}
	}
}