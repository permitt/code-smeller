        public ProductPromoUseInfo(String productPromoId, String productPromoCodeId, BigDecimal totalDiscountAmount, BigDecimal quantityLeftInActions, Map<ShoppingCartItem,BigDecimal> usageInfoMap) {
            this.productPromoId = productPromoId;
            this.productPromoCodeId = productPromoCodeId;
            this.totalDiscountAmount = totalDiscountAmount;
            this.quantityLeftInActions = quantityLeftInActions;
            this.usageInfoMap = usageInfoMap;
        }