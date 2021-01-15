  public Geo3dRectangleShape(final GeoBBox shape,
                             final SpatialContext spatialcontext,
                             double minX,
                             double maxX,
                             double minY,
                             double maxY) {
    super(shape, spatialcontext);
    this.minX = minX;
    this.maxX = maxX;
    this.minY = minY;
    this.maxY = maxY;
  }