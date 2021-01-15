    @Override
    public void setDefaults(ILaunchConfigurationWorkingCopy configuration) {
        launchConfigurationWorkingCopy = configuration;

        if (noToolCombo)
            configuration.setAttribute(LaunchConfigurationConstants.ATTR_TOOL, tool);
        else
            configuration.setAttribute(LaunchConfigurationConstants.ATTR_TOOL, LaunchConfigurationConstants.DEFAULT_TOOL);
        configuration.setAttribute(LaunchConfigurationConstants.ATTR_GENERAL_TRACECHILD, LaunchConfigurationConstants.DEFAULT_GENERAL_TRACECHILD);
        configuration.setAttribute(LaunchConfigurationConstants.ATTR_GENERAL_FREERES, LaunchConfigurationConstants.DEFAULT_GENERAL_FREERES);

        configuration.setAttribute(LaunchConfigurationConstants.ATTR_GENERAL_DEMANGLE, LaunchConfigurationConstants.DEFAULT_GENERAL_DEMANGLE);
        configuration.setAttribute(LaunchConfigurationConstants.ATTR_GENERAL_NUMCALLERS, LaunchConfigurationConstants.DEFAULT_GENERAL_NUMCALLERS);
        configuration.setAttribute(LaunchConfigurationConstants.ATTR_GENERAL_ERRLIMIT, LaunchConfigurationConstants.DEFAULT_GENERAL_ERRLIMIT);
        configuration.setAttribute(LaunchConfigurationConstants.ATTR_GENERAL_BELOWMAIN, LaunchConfigurationConstants.DEFAULT_GENERAL_BELOWMAIN);
        configuration.setAttribute(LaunchConfigurationConstants.ATTR_GENERAL_MAXFRAME, LaunchConfigurationConstants.DEFAULT_GENERAL_MAXFRAME);
        configuration.setAttribute(LaunchConfigurationConstants.ATTR_GENERAL_SUPPFILES, LaunchConfigurationConstants.DEFAULT_GENERAL_SUPPFILES);

        // 3.4.0 specific
        if (valgrindVersion == null || valgrindVersion.compareTo(ValgrindLaunchPlugin.VER_3_4_0) >= 0) {
            configuration.setAttribute(LaunchConfigurationConstants.ATTR_GENERAL_MAINSTACK_BOOL, LaunchConfigurationConstants.DEFAULT_GENERAL_MAINSTACK_BOOL);
            configuration.setAttribute(LaunchConfigurationConstants.ATTR_GENERAL_MAINSTACK, LaunchConfigurationConstants.DEFAULT_GENERAL_MAINSTACK);
        }

        // 3.6.0 specific
        if (valgrindVersion == null || valgrindVersion.compareTo(ValgrindLaunchPlugin.VER_3_6_0) >= 0) {
            configuration.setAttribute(LaunchConfigurationConstants.ATTR_GENERAL_DSYMUTIL, LaunchConfigurationConstants.DEFAULT_GENERAL_DSYMUTIL);
            configuration.setAttribute(LaunchConfigurationConstants.ATTR_FULLPATH_AFTER, LaunchConfigurationConstants.DEFAULT_FULLPATH_AFTER);
        }

        if (dynamicTab != null) {
            dynamicTab.setDefaults(configuration);
            initDefaults = false;
        }
    }