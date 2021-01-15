  protected AccessibleEditPart getAccessibleEditPart() {
		
	  if (accessiblePart ==null)
	  {
		  accessiblePart = new AccessibleGraphicalEditPart(){
		
			public void getName(AccessibleEvent e) {		 
				e.result = getReaderText();
			}
		};
	  }
	  return accessiblePart;
	}