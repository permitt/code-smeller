        public AuthorizationData getAuthzData() {
            if (authzData == null) {
                authzData = getFieldAs(IntendedForApplicationClassField.IFAC_elements, AuthorizationData.class);
            }
            return authzData;
        }