    protected void runFunctions(final CommandHandler handler) throws Exception {        
        handler.runCommandWithReturnCodeCheck(
                getStartFunctionHostCommand(),
                true, /* showStdout */
                getDeploymentStagingDirectoryPath(),
                CommandUtils.getValidReturnCodes(),
                RUN_FUNCTIONS_FAILURE
        );
    }