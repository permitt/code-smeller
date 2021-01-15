	@Test
	public void createsTextWithAllProperties() {
		final TypedEvent[] raisedEvents = new TypedEvent[3];
		Text text = TextFactory.newText(SWT.NONE).text("Test Text").message("message").limitTo(10)
				.onSelect(e -> raisedEvents[0] = e)
				.onModify(e -> raisedEvents[1] = e)
				.onVerify(e -> raisedEvents[2] = e)

				.create(shell);

		text.notifyListeners(SWT.Selection, new Event());
		text.notifyListeners(SWT.Modify, new Event());
		text.notifyListeners(SWT.Verify, new Event());

		assertEquals("Test Text", text.getText());
		assertEquals("message", text.getMessage());
		assertEquals(10, text.getTextLimit());

		assertEquals(1, text.getListeners(SWT.Selection).length);
		assertNotNull(raisedEvents[0]);

		assertEquals(1, text.getListeners(SWT.Modify).length);
		assertNotNull(raisedEvents[1]);

		assertEquals(1, text.getListeners(SWT.Verify).length);
		assertNotNull(raisedEvents[2]);
	}