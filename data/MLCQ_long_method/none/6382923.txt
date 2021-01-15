    private void setInitialDefault(String dir) {
        if (dir == null || dir.length() <= 0) {
            initialDefault = null;
            return;
        }

        dir = new Path(dir).toOSString();
        while (dir.charAt(dir.length() - 1) == File.separatorChar) {
			dir = dir.substring(0, dir.length() - 1);
		}
        initialDefault = dir;
    }