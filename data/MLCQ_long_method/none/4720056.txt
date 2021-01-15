    @Override
    public void generateGroovy(GroovyGenerationContext context) {
        context.append(label);
        context.append(":");
        expr.generateGroovy(context);
    }