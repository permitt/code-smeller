    public static synchronized HeapDumpOnOOMEAction instance() {
        if (instance == null) 
            instance = new HeapDumpOnOOMEAction();
        return instance;
    }