public class IncludeTransform implements Transform {

    //~ Methods **************************************************************************************************************************************

    @Override
    public List<Metric> transform(QueryContext context, List<Metric> metrics) {
        throw new UnsupportedOperationException("Include Transform cannot be performed without an regular expression.");
    }

    @Override
    public List<Metric> transform(QueryContext queryContext, List<Metric> metrics, List<String> constants) {
        SystemAssert.requireArgument(metrics != null, "Cannot transform null metric/metrics");
        SystemAssert.requireArgument(constants != null && constants.size() == 1,
            "Include transform require regex, only exactly one constant allowed.");
        SystemAssert.requireArgument(!constants.get(0).equals(""), "Expression can't be an empty string");

        List<Metric> includeMetricList = new ArrayList<Metric>();
        String expr = constants.get(0);

        for (Metric metric : metrics) {
            String name = metric.getIdentifier();
            boolean isMatch = name.matches(expr);

            if (isMatch) {
                includeMetricList.add(metric);
            }
        }
        return includeMetricList;
    }

    @Override
    public String getResultScopeName() {
        return TransformFactory.Function.INCLUDE.name();
    }

    @Override
    public List<Metric> transform(QueryContext queryContext, List<Metric>... listOfList) {
        throw new UnsupportedOperationException("Include doesn't need list of list!");
    }
}