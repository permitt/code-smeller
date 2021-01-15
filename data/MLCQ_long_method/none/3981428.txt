    public ConstraintModel( Annotation annotation, Class<? extends Constraint<?, ?>> constraintClass )
    {
        super( annotation );
        this.constraintClass = constraintClass;
    }