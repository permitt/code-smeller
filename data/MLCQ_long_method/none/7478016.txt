    public boolean isReference() {
        if (isCachedLanguage()) {
            return !ElementUtils.typeEquals(getLanguageType(), getParameter().getType());
        } else {
            return ElementUtils.typeEquals(getReferenceType(), getParameter().getType());
        }
    }