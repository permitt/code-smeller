    public boolean hasPermission(String domain, GwtSessionPermissionAction action, GwtSessionPermissionScope targetScope) {
        return hasPermission(new GwtSessionPermission(domain, action, targetScope));
    }