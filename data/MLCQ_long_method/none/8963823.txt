    @Override
    public AggregateCall other(RelDataTypeFactory typeFactory, AggregateCall e) {
      return AggregateCall.create(
          new HiveSqlCountAggFunction(isDistinct, returnTypeInference, operandTypeInference, operandTypeChecker),
          false, ImmutableIntList.of(), -1,
          typeFactory.createTypeWithNullability(typeFactory.createSqlType(SqlTypeName.BIGINT), true), "count");
    }