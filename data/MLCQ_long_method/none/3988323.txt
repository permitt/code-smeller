    void updateEntity( UnitOfWork current )
    {
        try
        {
            entity = current.get( entity );
        }
        catch( NoSuchEntityException e )
        {
            // Entity was deleted
            entity = null;
        }
    }