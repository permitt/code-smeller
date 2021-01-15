	private class SpellingProblemCollector
			implements ISpellingProblemCollector {

		SpellingProblemCollector() {
		}

		@Override
		public void accept(SpellingProblem problem) {
			final IProblemRequestor requestor = fRequestor;
			if (requestor != null) {
				try {
					final IDocument document = getDocument();
					int line = document.getLineOfOffset(problem.getOffset())
							+ 1;
					String word = document.get(problem.getOffset(),
							problem.getLength());
					// boolean dictionaryMatch= false;
					// boolean sentenceStart= false;
					// if (problem instanceof JavaSpellingProblem) {
					// dictionaryMatch=
					// ((JavaSpellingProblem)problem).isDictionaryMatch();
					// sentenceStart= ((JavaSpellingProblem)
					// problem).isSentenceStart();
					// }
					// see https://bugs.eclipse.org/bugs/show_bug.cgi?id=81514
					IEditorInput editorInput = fEditor.getEditorInput();
					if (editorInput != null) {
						ScriptSpellingProblem iProblem = new ScriptSpellingProblem(
								problem.getOffset(),
								problem.getOffset() + problem.getLength(), line,
								problem.getMessage(), word,
								false /* dictionaryMatch */,
								false /* sentenceStart */, document,
								editorInput.getName(), problem);
						requestor.acceptProblem(iProblem);
					}
				} catch (BadLocationException x) {
					// drop this SpellingProblem
				}
			}
		}

		@Override
		public void beginCollecting() {
			if (fRequestor != null)
				fRequestor.beginReporting();
		}

		@Override
		public void endCollecting() {
			if (fRequestor != null)
				fRequestor.endReporting();
		}
	}