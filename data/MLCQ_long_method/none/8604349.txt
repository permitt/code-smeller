        private void advance() {
            while (nextIdx < locParts.length()) {
                GridDhtLocalPartition part = locParts.get(nextIdx);

                if (part != null && part.state().active()) {
                    nextPart = part;
                    return;
                }

                nextIdx++;
            }
        }