public class ASCIIDecoder extends AbstractCharDecoder {
    
    /**
     * Creates a new ASCIIDecoder.
     */
    public ASCIIDecoder(InputStream is) {
        super(is);
    }

    /**
     * Reads the next character.
     * @return a character or END_OF_STREAM.
     */
    public int readChar() throws IOException {
        if (position == count) {
            fillBuffer();
        }
        if (count == -1) {
            return END_OF_STREAM;
        }
        int result = buffer[position++];
        if (result < 0) {
            charError("ASCII");
        }
        return result;
    }
}