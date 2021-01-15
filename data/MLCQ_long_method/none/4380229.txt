    public static boolean accept(AST node) {
        return TypedefVisitor.accept(node)
            || StructVisitor.accept(node)
            || UnionVisitor.accept(node)
            || EnumVisitor.accept(node);
    }