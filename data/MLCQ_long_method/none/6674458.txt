	@Override
	protected void formatPost(IJSONNode node, IRegion region, StringBuilder source) {
		IJSONCleanupStrategy stgy = getCleanupStrategy(node);

		if (region.getOffset() >= 0 && region.getLength() >= 0) {
			IStructuredDocument document = node.getOwnerDocument().getModel().getStructuredDocument();
			CompoundRegion[] regions = getRegionsWithoutWhiteSpaces(document, region, stgy);
			if (regions.length > 0 && regions[regions.length - 1] != null) {
				CompoundRegion r = regions[regions.length - 1];
				if (r != null && r.getType() == JSONRegionContexts.JSON_ARRAY_CLOSE) {
					source.append(decoratedRegion(r, 0, stgy));
				}
			}
		}
	}