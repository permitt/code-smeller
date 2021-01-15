    void commandLoop() {
        try {
            while (processCommand()) {
                // condition is loop action
            }
        } catch (IOException ex) {
            // drop out of loop
        }
    }