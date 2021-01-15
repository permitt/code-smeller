        @Override
        public Object clone() {
            AFPData obj = (AFPData) super.clone();
            obj.filled = this.filled;
            obj.imageUri = this.imageUri;
            return obj;
        }