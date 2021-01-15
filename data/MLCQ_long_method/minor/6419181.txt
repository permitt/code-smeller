    private Class getCommonResourceClass(List objects) {
        if (objects == null || objects.isEmpty()) {
            return null;
        }
        Class resourceClass = LegacyResourceSupport.getResourceClass();
        if (resourceClass == null) {
            // resources plug-in not loaded - no resources. period.
            return null;
        }

        List testList = new ArrayList(objects.size());

        for (int i = 0; i < objects.size(); i++) {
            Object object = objects.get(i);

            if (object instanceof IAdaptable) {
                if (resourceClass.isInstance(object)) {
                    continue;
                }

                Object resource = LegacyResourceSupport
                        .getAdaptedContributorResource(object);

                if (resource == null) {
                    //Not a resource and does not adapt. No common resource class
                    return null;
                }
                testList.add(resource);
            } else {
                return null;
            }
        }

        return getCommonClass(testList);
    }