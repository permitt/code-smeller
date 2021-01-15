    public GraphVisualizer() {
        model = new CachingStatCalculator("Graph");
        graph = new Graph(model);
        init();
    }