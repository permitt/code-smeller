        @Override
        public boolean hasNext()
        {
            return this.currentIndex != CodePointAdapter.this.adapted.length();
        }