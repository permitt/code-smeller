    public static void main(String[] args) throws Exception {
        isLocal = false;
        conf = JStormHelper.getConfig(args);
        if (args.length != 0) {
            spoutSingle = false;
        }
        test();
    }