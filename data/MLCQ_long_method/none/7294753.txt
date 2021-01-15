        @SuppressWarnings("rawtypes")
        protected Class createClass(byte[] code, ClassNode classNode) {
            theClass = classNode;
            return super.createClass(code, classNode);
        }