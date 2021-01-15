    private void validate()
    {
        setPageComplete( getApplyOnDns() != null || spw.isValid() );
        setErrorMessage( searchButton.getSelection() ? spw.getErrorMessage() : null );
    }