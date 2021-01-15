public class DefaultReceivePackFactory implements
		ReceivePackFactory<HttpServletRequest> {
	private static class ServiceConfig {
		final boolean set;

		final boolean enabled;

		ServiceConfig(Config cfg) {
			set = cfg.getString("http", null, "receivepack") != null;
			enabled = cfg.getBoolean("http", "receivepack", false);
		}
	}

	/** {@inheritDoc} */
	@Override
	public ReceivePack create(HttpServletRequest req, Repository db)
			throws ServiceNotEnabledException, ServiceNotAuthorizedException {
		final ServiceConfig cfg = db.getConfig().get(ServiceConfig::new);
		String user = req.getRemoteUser();

		if (cfg.set) {
			if (cfg.enabled) {
				if (user == null || "".equals(user))
					user = "anonymous";
				return createFor(req, db, user);
			}
			throw new ServiceNotEnabledException();
		}

		if (user != null && !"".equals(user))
			return createFor(req, db, user);
		throw new ServiceNotAuthorizedException();
	}

	private static ReceivePack createFor(final HttpServletRequest req,
			final Repository db, final String user) {
		final ReceivePack rp = new ReceivePack(db);
		rp.setRefLogIdent(toPersonIdent(req, user));
		return rp;
	}

	private static PersonIdent toPersonIdent(HttpServletRequest req, String user) {
		return new PersonIdent(user, user + "@" + req.getRemoteHost());
	}
}