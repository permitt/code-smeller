    protected ResultSet executeQuery(Connection conn, PreparedStatement stmnt,
        SQLBuffer sql) throws SQLException {
        return stmnt.executeQuery();
    }