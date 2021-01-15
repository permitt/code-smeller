    @Override
    public List<PlainSchema> findByKeyword(final String keyword) {
        TypedQuery<PlainSchema> query = entityManager().createQuery(
                "SELECT e FROM " + JPAPlainSchema.class.getSimpleName() + " e"
                + " WHERE e.id LIKE :keyword", PlainSchema.class);
        query.setParameter("keyword", keyword);
        return query.getResultList();
    }