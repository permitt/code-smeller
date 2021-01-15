    protected SignatureVisitor createSignatureRemapper(final SignatureVisitor signatureVisitor) {
        return new SignatureRemapper(signatureVisitor, this);
    }