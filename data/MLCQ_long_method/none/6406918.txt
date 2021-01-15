		private boolean styleSelected(Item selection) {
			CSSStyleDeclaration selectedStyle = engine.getViewCSS()
					.getComputedStyle(engine.getElement(selection), "selected");
			if (selectedStyle == null) {
				return false;
			}

			applyStyles(selectedStyle, "selected", selection);
			return true;
		}