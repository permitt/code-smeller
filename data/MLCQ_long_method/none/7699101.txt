    @Override
    public boolean is2G(){
        LuaJavaNetworkState state = new LuaJavaNetworkState(mRapidID, mRapidView);

        return state.isNetworkActive();
    }