    public static Element getParent(Element elem) {
        Node parent = elem.getParentNode();
        if (parent instanceof Element)
            return (Element)parent;
        return null;
    } // getParent(Element):Element