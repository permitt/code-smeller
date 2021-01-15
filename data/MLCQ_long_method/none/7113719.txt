    public static StringBuffer formatInput(StringBuffer appendTo,
                                           Replaceable input,
                                           Transliterator.Position pos) {
        return formatInput(appendTo, (ReplaceableString) input, pos);
    }