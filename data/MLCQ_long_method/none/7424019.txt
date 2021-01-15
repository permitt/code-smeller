        protected ZeroNullConversionOp(LIRInstructionClass<? extends ZeroNullConversionOp> type, AllocatableValue result, AllocatableValue input) {
            super(type);
            this.result = result;
            this.input = input;
        }