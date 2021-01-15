public final class DocumentSetupParticipant implements IDocumentSetupParticipant {
	private final TTCN3Editor editor;

	public DocumentSetupParticipant(final TTCN3Editor editor) {
		this.editor = editor;
	}

	/*
	 * (non-Javadoc)
	 *
	 * @see
	 * org.eclipse.core.filebuffers.IDocumentSetupParticipant#setup(org.
	 * eclipse.jface.text.IDocument)
	 */
	@Override
	public void setup(final IDocument document) {
		DocumentTracker.put((IFile) editor.getEditorInput().getAdapter(IFile.class), document);

		final IDocumentPartitioner partitioner = new FastPartitioner(new PartitionScanner(), PartitionScanner.PARTITION_TYPES);
		if (document instanceof IDocumentExtension3) {
			final IDocumentExtension3 extension3 = (IDocumentExtension3) document;
			extension3.setDocumentPartitioner(PartitionScanner.TTCN3_PARTITIONING, partitioner);
		} else {
			document.setDocumentPartitioner(partitioner);
		}
		partitioner.connect(document);

		document.addDocumentListener(new IDocumentListener() {

			@Override
			public void documentAboutToBeChanged(final DocumentEvent event) {
				GlobalIntervalHandler.putInterval(event.getDocument(), null);
			}

			@Override
			public void documentChanged(final DocumentEvent event) {
				//Do nothing
			}

		});
	}
}