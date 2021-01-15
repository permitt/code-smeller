    public void dispose() {
        this.decommission( this.instance );
        this.instance = null;

        super.dispose();
    }