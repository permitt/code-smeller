        public GenericRequestMapper<Input, Output> build() {
            return new BaseRequestMapper<>(handlerChains);
        }