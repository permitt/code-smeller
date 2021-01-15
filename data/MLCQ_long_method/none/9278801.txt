    public CharsetDecoder newDecoder() {
        return new Decoder(this, plane);
    }