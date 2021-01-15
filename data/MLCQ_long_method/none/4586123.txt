    public int bidiLevelAt(int position) throws IndexOutOfBoundsException {
        if ((position < 0) || (position >= length())) {
            throw new IndexOutOfBoundsException();
        } else if (bidiLevels != null) {
            return bidiLevels [ position ];
        } else {
            return -1;
        }
    }