		public ConsoleView build() {
			final ConsoleView consoleView = Mockito.mock(ConsoleView.class);
			Mockito.when(consoleView.getConsoleText()).thenReturn(this.msg);
			return consoleView;
		}