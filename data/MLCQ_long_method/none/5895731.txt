    public static <S, T> HashMapBuilder<S, T> hashMap( S key, T value ) {
        return new HashMapBuilder<S, T>().map( key, value );
    }