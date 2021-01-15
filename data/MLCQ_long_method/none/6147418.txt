		@Override
		public void mouseDown(MouseEvent e) {
			Item item = (Item) ((Widget) e.getSource()).getData();
			// TODO for now, to make double click work: disable single click on
			// the first item
			// disable later when the annotationlistener selectively handles
			// input
			if (item != null && e.button == 1) // && item.fAnnotation !=
												// fInput.fAnnotations[0])
				item.defaultSelected();
		}