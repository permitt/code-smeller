        @Override
        public void writeToBuffer(QpidByteBuffer buffer)
        {
            _type.writeToBuffer(_value, buffer);
        }