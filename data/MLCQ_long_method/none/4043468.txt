    public UnionAllOperatorDescriptor(IOperatorDescriptorRegistry spec, int nInputs,
            RecordDescriptor recordDescriptor) {
        super(spec, nInputs, 1);
        outRecDescs[0] = recordDescriptor;
    }