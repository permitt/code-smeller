public class FormatActivator implements BundleActivator {
	/**
	 * {@inheritDoc}
	 *
	 * Registers all included archive formats by calling
	 * {@link ArchiveFormats#registerAll()}. This method is called by the OSGi
	 * framework when the bundle is started.
	 */
	@Override
	public void start(BundleContext context) {
		ArchiveFormats.registerAll();
	}

	/**
	 * {@inheritDoc}
	 *
	 * Cleans up after {@link #start(BundleContext)} by calling
	 * {@link ArchiveFormats#unregisterAll}.
	 */
	@Override
	public void stop(BundleContext context) {
		ArchiveFormats.unregisterAll();
	}
}