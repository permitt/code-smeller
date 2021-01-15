    public static boolean isVirtualStackSlot(Value value) {
        assert value != null;
        return value instanceof VirtualStackSlot;
    }