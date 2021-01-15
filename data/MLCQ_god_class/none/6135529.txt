public interface IInterpreterRunner {
	public void run(InterpreterConfig config,
			ILaunch launch, IProgressMonitor monitor) throws CoreException;

}