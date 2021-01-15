    class SimpleColumnHeaderDataProvider implements IDataProvider {

        @Override
        public Object getDataValue(int columnIndex, int rowIndex) {
            return "Column " + (columnIndex + 1); //$NON-NLS-1$
        }

        @Override
        public void setDataValue(int columnIndex, int rowIndex, Object newValue) {
            throw new UnsupportedOperationException();
        }

        @Override
        public int getColumnCount() {
            return _304_DynamicColumnExample.this.columns.size();
        }

        @Override
        public int getRowCount() {
            return 1;
        }

    }