	private static class MaskProcessor extends XMLProcessor {
		private OpUnitMask.MaskInfo info;

		@Override
		public void reset(Object callData) {
			info = new OpUnitMask.MaskInfo();
		}

		@Override
		public void endElement(String name, Object callData) {
			if (name.equals(VALUE_TAG)) {
				// Set mask's value
				info.value = Integer.parseInt(characters);
			} else if (name.equals(DESCRIPTION_TAG)) {
				info.description = characters;
			} else if (name.equals(NAME_TAG)) {
				info.name = characters;
			} else if (name.equals(MASK_TAG)) {
				// Pop and pass mask tag to previous processor (UnitMaskProcessor)
				OprofileSAXHandler.getInstance(callData).pop(MASK_TAG);
			}
		}

		/**
		 * Returns the information that has been collected about a mask.
		 * 
		 * @return the mask information
		 */
		public OpUnitMask.MaskInfo getResult() {
			return info;
		}
	}