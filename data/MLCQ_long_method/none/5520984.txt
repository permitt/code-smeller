    @Override
    public void setRememberMeServices(RememberMeServices rememberMeServices) {
	if (logger.isDebugEnabled()) {
	    logger.debug("setRememberMeServices() enter: rememberMeServices="
		    + rememberMeServices.toString());
	}
	super.setRememberMeServices(rememberMeServices);
    }