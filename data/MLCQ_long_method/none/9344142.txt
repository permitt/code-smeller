        public void stateChanged(ChangeEvent e) {
            if (!isDragging) {
                calculateThumbLocation();
                slider.repaint();
            }
            lastValue = slider.getValue();
        }