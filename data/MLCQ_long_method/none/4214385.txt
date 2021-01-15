    public void initialize(BSFManager mgr, String lang,Vector declaredBeans)
    throws BSFException
    {
        super.initialize(mgr, lang, declaredBeans);
        mgrfuncs = new BSFFunctions (mgr, this);
    }