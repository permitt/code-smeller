public interface IShellProvider {
    /**
     * Returns the current shell (or null if none). This return value may
     * change over time, and should not be cached.
     *
     * @return the current shell or null if none
     */
    Shell getShell();
}