    public TypeElementCatalog(Iterable<TypeElement> typeElements, Configuration config) {
        this(config);
        for (TypeElement typeElement : typeElements) {
            addTypeElement(typeElement);
        }
    }