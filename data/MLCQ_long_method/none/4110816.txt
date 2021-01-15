        @Override
        public Boolean handleAddCatalogItem(Object catalogItemBeingAdded) {
            return isEntitledToAddCatalogItem(context, catalogItemBeingAdded);
        }