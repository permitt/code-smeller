    public static class RefRec {
        public RefRec(Object id, Object value) {
            this.id = id;
            this.value = value;
            addRef();
        }

        public Object getId() {
            return id;
        }

        public Object getValue() {
            return value;
        }

        public int addRef() {
            ++refCount;
            return refCount;
        }

        public int removeRef() {
            --refCount;
            return refCount;
        }

        public int getRef() {
            return refCount;
        }

        public boolean isNotReferenced() {
            return (refCount <= 0);
        }

        public Object id;

        public Object value;

        private int refCount;
    }