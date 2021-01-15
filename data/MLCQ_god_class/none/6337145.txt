public class DockerConfiguration extends TextSourceViewerConfiguration {

	private DockerEditor editor;
	private DockerHover hover;

	public DockerConfiguration(DockerEditor editor) {
		this.editor = editor;
	}

	@Override
	public IPresentationReconciler getPresentationReconciler(ISourceViewer sourceViewer) {
		return new DockerPresentationReconciler();
	}

	@Override
	public IReconciler getReconciler(ISourceViewer sourceViewer) {
		Reconciler reconciler = new Reconciler();
		IReconcilingStrategy strategy = new SyntaxReconcilingStrategy(editor);
		reconciler.setReconcilingStrategy(strategy, IDocument.DEFAULT_CONTENT_TYPE);
		return reconciler;
	}

	@Override
	public IContentAssistant getContentAssistant(ISourceViewer sourceViewer) {
		ContentAssistant ca = new ContentAssistant();
		IContentAssistProcessor cap = new CompletionProcessor();
		ca.setContentAssistProcessor(cap, IDocument.DEFAULT_CONTENT_TYPE);
		ca.setInformationControlCreator(getInformationControlCreator(sourceViewer));
		return ca;
	}

	@Override
	public ITextHover getTextHover(ISourceViewer sourceViewer, String contentType) {
		if (hover == null) {
			hover = new DockerHover();
		}
		return hover;
	}

}