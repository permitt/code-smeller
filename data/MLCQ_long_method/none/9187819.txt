		public void inputChanged( Viewer viewer, Object oldInput,
				Object newInput )
		{
			if ( viewer == subCategoryTable )
			{
				functionTable.setInput( null );
			}
		}