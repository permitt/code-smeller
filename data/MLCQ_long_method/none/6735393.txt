	public void testMangleMultipleServerSide2InJSCheckProblems() {
		// get model
		String fileName = getName() + ".html";
		IStructuredModel structuredModel = getSharedModel(fileName, "<script> var text = <? serverObject.getText() ?>;  <? serverObject.getText() ?></script>");
		assertNotNull("missing test model", structuredModel);
		
		// do translation
		JsTranslationAdapterFactory.setupAdapterFactory(structuredModel);
		JsTranslationAdapter translationAdapter = (JsTranslationAdapter) ((IDOMModel) structuredModel).getDocument().getAdapterFor(IJsTranslation.class);
		IJsTranslation translation = translationAdapter.getJsTranslation(false);
		String translated = translation.getJsText();
		assertTrue("translation empty", translated.length() > 5);
		assertTrue("server-side script block included", translated.indexOf("<?") < 0);
		assertTrue("server-side script block included", translated.indexOf("?>") < 0);
		assertTrue("var dropped", translated.indexOf("var text = ") > -1);
		assertTrue("problems found in translation ", translation.getProblems().isEmpty());

		// release model
		structuredModel.releaseFromRead();
	}