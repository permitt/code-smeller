    @GET
    @Path("list")
    public Collection<Subject> list() {
        return dao.findAll();
    }