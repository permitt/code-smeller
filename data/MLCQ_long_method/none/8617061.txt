    public void onBeforeWrite() {
        if (req && reqSndTs == 0) {
            reqSndTs = System.nanoTime();

            reqSndTsMillis = System.currentTimeMillis();
        }

        if (!req && resSndTs == 0) {
            resSndTs = System.nanoTime();

            resSndTsMillis = System.currentTimeMillis();
        }
    }