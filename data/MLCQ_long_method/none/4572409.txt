        static GlyphSubstitutionSubtable create(String id, int sequence, int flags, int format, GlyphCoverageTable coverage, List entries) {
            if (format == 1) {
                return new ReverseChainedSingleSubtableFormat1(id, sequence, flags, format, coverage, entries);
            } else {
                throw new UnsupportedOperationException();
            }
        }