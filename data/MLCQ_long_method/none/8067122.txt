		public TitanBoolean constGet_at( final int index_value ) {
			must_bound( "Accessing an element in an unbound value of type @PreGenRecordOf.PREGEN_SET_OF_BOOLEAN_OPTIMIZED." );
			if (index_value < 0) {
				throw new TtcnError( "Accessing an element of type @PreGenRecordOf.PREGEN_SET_OF_BOOLEAN_OPTIMIZED using a negative index: "+index_value+".");
			}
			final int nofElements = n_elem().get_int();
			if ( index_value >= nofElements ) {
				throw new TtcnError( "Index overflow in a value of type @PreGenRecordOf.PREGEN_SET_OF_BOOLEAN_OPTIMIZED: The index is "+index_value+", but the value has only "+nofElements+" elements." );
			}

			final TitanBoolean elem = valueElements.get( index_value );
			return ( elem == null ) ? get_unbound_elem(): elem ;
		}