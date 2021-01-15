  @Nullable
  public final QualifiedName getQualifiedNameObject() {
    return isQualifiedName() ? new QualifiedName.NodeQname(this) : null;
  }