public class DTDTemplatePreferencePage extends TemplatePreferencePage {

	class DTDEditTemplateDialog extends EditTemplateDialog {
		public DTDEditTemplateDialog(Shell parent, Template template, boolean edit, boolean isNameModifiable, ContextTypeRegistry registry) {
			super(parent, template, edit, isNameModifiable, registry);
		}

		protected SourceViewer createViewer(Composite parent) {
			SourceViewerConfiguration sourceViewerConfiguration = new StructuredTextViewerConfiguration() {
				StructuredTextViewerConfiguration baseConfiguration = new StructuredTextViewerConfigurationDTD();

				public String[] getConfiguredContentTypes(ISourceViewer sourceViewer) {
					return baseConfiguration.getConfiguredContentTypes(sourceViewer);
				}

				public LineStyleProvider[] getLineStyleProviders(ISourceViewer sourceViewer, String partitionType) {
					return baseConfiguration.getLineStyleProviders(sourceViewer, partitionType);
				}

				public IContentAssistant getContentAssistant(ISourceViewer sourceViewer) {
					ContentAssistant assistant = new ContentAssistant();
					assistant.enableAutoActivation(true);
					assistant.enableAutoInsert(true);
					assistant.setContentAssistProcessor(getTemplateProcessor(), IDocument.DEFAULT_CONTENT_TYPE);
					return assistant;
				}
			};
			return doCreateViewer(parent, sourceViewerConfiguration);
		}
	}

	public DTDTemplatePreferencePage() {
		DTDUIPlugin dtdUIPlugin = DTDUIPlugin.getDefault();

		setPreferenceStore(dtdUIPlugin.getPreferenceStore());
		setTemplateStore(dtdUIPlugin.getTemplateStore());
		setContextTypeRegistry(dtdUIPlugin.getTemplateContextRegistry());
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see org.eclipse.jface.preference.IPreferencePage#performOk()
	 */
	public boolean performOk() {
		boolean ok = super.performOk();
		DTDUIPlugin.getDefault().savePluginPreferences();
		return ok;
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see org.eclipse.ui.texteditor.templates.TemplatePreferencePage#isShowFormatterSetting()
	 */
	protected boolean isShowFormatterSetting() {
		// template formatting has not been implemented
		return false;
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see org.eclipse.jface.preference.PreferencePage#createContents(org.eclipse.swt.widgets.Composite)
	 */
	protected Control createContents(Composite ancestor) {
		Control c = super.createContents(ancestor);
		PlatformUI.getWorkbench().getHelpSystem().setHelp(c, IHelpContextIds.DTD_PREFWEBX_TEMPLATES_HELPID);
		return c;
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see org.eclipse.ui.texteditor.templates.TemplatePreferencePage#createViewer(org.eclipse.swt.widgets.Composite)
	 */
	protected SourceViewer createViewer(Composite parent) {
		SourceViewerConfiguration sourceViewerConfiguration = new StructuredTextViewerConfiguration() {
			StructuredTextViewerConfiguration baseConfiguration = new StructuredTextViewerConfigurationDTD();

			public String[] getConfiguredContentTypes(ISourceViewer sourceViewer) {
				return baseConfiguration.getConfiguredContentTypes(sourceViewer);
			}

			public LineStyleProvider[] getLineStyleProviders(ISourceViewer sourceViewer, String partitionType) {
				return baseConfiguration.getLineStyleProviders(sourceViewer, partitionType);
			}
		};
		return doCreateViewer(parent, sourceViewerConfiguration);
	}

	SourceViewer doCreateViewer(Composite parent, SourceViewerConfiguration viewerConfiguration) {
		SourceViewer viewer = null;
		String contentTypeID = ContentTypeIdForDTD.ContentTypeID_DTD;
		viewer = new StructuredTextViewer(parent, null, null, false, SWT.BORDER | SWT.V_SCROLL | SWT.H_SCROLL);
		viewer.getTextWidget().setFont(JFaceResources.getFont("org.eclipse.wst.sse.ui.textfont")); //$NON-NLS-1$
		IStructuredModel scratchModel = StructuredModelManager.getModelManager().createUnManagedStructuredModelFor(contentTypeID);
		IDocument document = scratchModel.getStructuredDocument();
		viewer.configure(viewerConfiguration);
		viewer.setDocument(document);
		return viewer;
	}

	/**
	 * Creates the edit dialog. Subclasses may override this method to provide
	 * a custom dialog.
	 * 
	 * @param template
	 *            the template being edited
	 * @param edit
	 *            whether the dialog should be editable
	 * @param isNameModifiable
	 *            whether the template name may be modified
	 * @return the created or modified template, or <code>null</code> if the
	 *         edition failed
	 * @since 3.1
	 */
	protected Template editTemplate(Template template, boolean edit, boolean isNameModifiable) {
		EditTemplateDialog dialog = new DTDEditTemplateDialog(getShell(), template, edit, isNameModifiable, getContextTypeRegistry());
		if (dialog.open() == Window.OK) {
			return dialog.getTemplate();
		}
		return null;
	}
}