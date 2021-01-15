		private final class MyPage extends WizardPage {
			private Button fCloseButton;

			private MyPage(String pPageName, String pTitle, ImageDescriptor pTitleImage) {
				super(pPageName, pTitle, pTitleImage);
			}

			@Override
			public void createControl(Composite pParent) {
				fCloseButton = new Button(pParent, SWT.CHECK);
				fCloseButton.setText("Close wizard after progress is complete");
				setControl(fCloseButton);
			}

			public boolean isCloseWanted() {
				return fCloseButton.getSelection();
			}
		}