        public int read(byte[] b) throws IOException {
            return readInternal(b, 0, b.length);
        }