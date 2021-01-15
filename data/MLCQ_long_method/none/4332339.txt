    public LdapClassLoader( DirectoryService directoryService ) throws LdapException
    {
        super( LdapClassLoader.class.getClassLoader() );
        this.directoryService = directoryService;
        defaultSearchDn = directoryService.getDnFactory().create( DEFAULT_SEARCH_CONTEXTS_CONFIG );

        objectClassAT = directoryService.getSchemaManager().getAttributeType( SchemaConstants.OBJECT_CLASS_AT );
    }