    @Override
    public String getOidByName( String name ) throws LdapException
    {
        return immutableMatchingRuleUseRegistry.getOidByName( name );
    }