    protected String getCsrfHeader() {
        Object csrfHeaderObject = getSession().get(SessionParameter.CSRF_HEADER);
        if (csrfHeaderObject instanceof String) {
            return (String) csrfHeaderObject;
        }

        return null;
    }