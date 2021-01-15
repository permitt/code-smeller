    private String getMetaDataValue(MetaDataHit mdh) throws FilterException
    {
        for (int i = 0; i < iv_metaFieldNames.length; i++)
        {
            String mdVal = mdh.getMetaFieldValue(iv_metaFieldNames[i]);
            if (mdVal != null)
            {
                return mdVal;
            }
        }
        throw new FilterException(
            new Exception("Unable to extract meta data from MetaDataHit object."));
    }