  DirectScanPrel(RelOptCluster cluster, RelTraitSet traits,
                 GroupScan groupScan, RelDataType rowType) {
    super(cluster, traits);
    this.groupScan = groupScan;
    this.rowType = rowType;
  }