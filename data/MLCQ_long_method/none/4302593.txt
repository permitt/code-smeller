    public synchronized void createPrincipal(String principal,
                                String password) throws KrbException {
        kadmin.addPrincipal(principal, password);
    }