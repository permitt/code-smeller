	private void updateWidgets() {
		MultiInstanceLoopCharacteristics lc = getBO();
		
		showCompletionConditionWidgets(lc.isIsSequential());
		
		if (lc!=null && !updatingWidgets) {
			updatingWidgets = true;
			switch (getInstanceType()) {
			case None:
				if (loopCardinalityButton!=null)
					loopCardinalityButton.setSelection(false);
				if (loopDataInputButton!=null)
					loopDataInputButton.setSelection(false);
				loopDataInputWidgetsShowing = true;
				loopCardinalityWidgetsShowing = true;
				showLoopDataInputWidgets(false);
				showLoopCardinalityWidgets(false);
				break;
			case LoopCardinality:
				if (loopCardinalityButton!=null)
					loopCardinalityButton.setSelection(true);
				if (loopDataInputButton!=null)
					loopDataInputButton.setSelection(false);
				showLoopDataInputWidgets(false);
				showLoopCardinalityWidgets(true);
				break;
			case DataInput:
				if (loopCardinalityButton!=null)
					loopCardinalityButton.setSelection(false);
				if (loopDataInputButton!=null)
					loopDataInputButton.setSelection(true);
				showLoopCardinalityWidgets(false);
				showLoopDataInputWidgets(true);
				break;
			}
			
			if (producesOutputButton!=null) {
				boolean producesOutput = (lc.getLoopDataOutputRef()!=null || lc.getOutputDataItem()!=null);
				producesOutputButton.setSelection(producesOutput);
				showLoopDataOutputWidgets(producesOutput);
			}
		}
		updatingWidgets = false;
	}