	protected void addNodeToCluster(final String name, final Set<NodeDescriptor> cluster) {
		final NodeDescriptor v = mapNameNode.get(name);
		cluster.add(v);
		v.setCluster(cluster);
	}