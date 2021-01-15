        boolean hasClasses() {
            Enumeration<? extends FileObject> e = pkg.getData(false);
            while (e.hasMoreElements())
                if (e.nextElement().getExt().equalsIgnoreCase("class")) // NOI18N
                    return true;
            return false;
        }