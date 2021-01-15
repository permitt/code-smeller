        public void declareVariable(String name) {
            declarations.append("declare variable ")
                .append("$")
                .append(name)
                .append(" external ")
                .append(";\n");
        }