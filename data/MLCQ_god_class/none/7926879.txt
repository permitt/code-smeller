	@SuppressWarnings("serial")
	class ShapeStyleList extends LinkedHashMap<Class, ShapeStyle> {
		public Category key;
		
		public ShapeStyleList(Category key) {
			this.key = key;
		}
	}