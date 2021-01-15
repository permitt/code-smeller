	protected ScriptDebugConsole createConsole(ILaunch launch) {
		final String encoding = selectEncoding(launch);
		final IProcess[] processes = launch.getProcesses();
		final IProcess process = processes.length != 0 ? processes[0] : null;
		final IConsoleColorProvider colorProvider = getColorProvider(
				process != null
						? process.getAttribute(IProcess.ATTR_PROCESS_TYPE)
						: null);
		final ScriptDebugConsole console = new ScriptDebugConsole(launch,
				computeName(launch), null, encoding, colorProvider);
		if (process != null) {
			console.setAttribute(IDebugUIConstants.ATTR_CONSOLE_PROCESS,
					process);
			if (process instanceof IScriptProcess) {
				console.connect((IScriptProcess) process);
			}
		}
		final IConsoleManager manager = getConsoleManager();
		manager.addConsoles(new IConsole[] { console });
		manager.showConsoleView(console);
		return console;
	}