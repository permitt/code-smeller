	public static void traceExecution(String processLabel,
			String[] cmdLineLabel, String[] environment) {
		StringBuffer sb = new StringBuffer();
		sb.append("-----------------------------------------------\n"); //$NON-NLS-1$
		sb.append("Running ").append(processLabel).append('\n'); //$NON-NLS-1$
		// sb.append("Command line: ").append(cmdLineLabel).append('\n');
		sb.append("Command line: "); //$NON-NLS-1$
		for (int i = 0; i < cmdLineLabel.length; i++) {
			sb.append(" " + cmdLineLabel[i]); //$NON-NLS-1$
		}
		sb.append("\n"); //$NON-NLS-1$
		sb.append("Environment:\n"); //$NON-NLS-1$
		for (int i = 0; i < environment.length; i++) {
			sb.append('\t').append(environment[i]).append('\n');
		}
		sb.append("-----------------------------------------------\n"); //$NON-NLS-1$
		System.out.println(sb);
	}