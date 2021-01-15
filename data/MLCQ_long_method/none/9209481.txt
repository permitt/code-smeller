    public DocumentCache(int size) throws SAXException {
        this(size, null);
        try {
            _dtmManager = XSLTCDTMManager.createNewDTMManagerInstance();
        } catch (Exception e) {
            throw new SAXException(e);
        }
    }