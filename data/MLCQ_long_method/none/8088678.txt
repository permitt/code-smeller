	@Override
	public boolean eIsSet(int featureID) {
		switch (featureID) {
			case AsubpackagePackage.AMODEL__ELEMENTS:
				return elements != null && !elements.isEmpty();
		}
		return super.eIsSet(featureID);
	}