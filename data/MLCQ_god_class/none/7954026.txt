	public static class PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template extends Record_Of_Template {

		//originally single_value/value_elements
		protected List<TitanUniversalCharString_template> value_elements;

		//originally value_list/list_value
		protected List<PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template> list_value;

		private final match_function_t match_function_specific = new match_function_t() {
			@Override
			public boolean match(final Base_Type value_ptr, final int value_index, final Restricted_Length_Template template_ptr, final int template_index, final boolean legacy) {
				return match_index((PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING)value_ptr, value_index, (PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template)template_ptr, template_index, legacy);
			}
		};

		/**
		 * Initializes to unbound/uninitialized template.
		 * */
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template() {
			// do nothing
		}

		/**
		 * Initializes to a given template kind.
		 *
		 * @param otherValue
		 *                the template kind to initialize to.
		 * */
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template(final template_sel otherValue ) {
			super( otherValue );
			check_single_selection( otherValue );
		}

		/**
		 * Initializes to a given value.
		 * The template becomes a specific template.
		 * The elements of the provided value are copied.
		 *
		 * @param otherValue
		 *                the value to initialize to.
		 * */
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template( final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING otherValue ) {
			copy_value( otherValue );
		}

		/**
		 * Initializes to a given template.
		 * The elements of the provided template are copied.
		 *
		 * @param otherValue
		 *                the value to initialize to.
		 * */
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template( final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template otherValue ) {
			copy_template( otherValue );
		}

		/**
		 * Initializes to a given value.
		 * The template becomes a specific template with the provided value.
		 * Causes a dynamic testcase error if the value is neither present nor optional.
		 *
		 * @param otherValue
		 *                the value to initialize to.
		 * */
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template( final Optional<PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING> otherValue ) {
			switch (otherValue.get_selection()) {
			case OPTIONAL_PRESENT:
				copy_value(otherValue.constGet());
				break;
			case OPTIONAL_OMIT:
				set_selection(template_sel.OMIT_VALUE);
				break;
			default:
				throw new TtcnError("Creating a template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING from an unbound optional field.");
			}
		}

		/**
		 * Initializes to an empty specific value template.
		 *
		 * @param nullValue
		 *                the null value.
		 * */
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template( final TitanNull_Type nullValue ) {
			super( template_sel.SPECIFIC_VALUE );
			value_elements = new ArrayList<TitanUniversalCharString_template>();
		}

		/**
		 * Internal function to copy the provided value into this template.
		 * The template becomes a specific value template.
		 * The already existing content is overwritten.
		 *
		 * @param other_value the value to be copied.
		 * */
		protected void copy_value(final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING other_value) {
			other_value.must_bound("Initialization of a template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING with an unbound value.");
			value_elements = new ArrayList<TitanUniversalCharString_template>();
			final int otherSize = other_value.valueElements.size();
			for (int elem_count = 0; elem_count < otherSize; elem_count++) {
				if (other_value.constGet_at(elem_count).is_bound()) {
					value_elements.add( new TitanUniversalCharString_template(other_value.constGet_at(elem_count)) );
				} else {
					value_elements.add( new TitanUniversalCharString_template() );
				}
			}
			set_selection(template_sel.SPECIFIC_VALUE);
		}

		/**
		 * Internal function to copy the provided template into this template.
		 * The already existing content is overwritten.
		 *
		 * @param other_value the value to be copied.
		 * */
		private void copy_template(final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template other_value) {
			switch (other_value.template_selection) {
			case SPECIFIC_VALUE:
				value_elements = new ArrayList<TitanUniversalCharString_template>();
				final int otherSize = other_value.value_elements.size();
				for (int elem_count = 0; elem_count < otherSize; elem_count++) {
					if (other_value.constGet_at(elem_count).is_bound()) {
						value_elements.add( new TitanUniversalCharString_template(other_value.constGet_at(elem_count)) );
					} else {
						value_elements.add( new TitanUniversalCharString_template() );
					}
				}
				break;
			case OMIT_VALUE:
			case ANY_VALUE:
			case ANY_OR_OMIT:
				break;
			case VALUE_LIST:
			case COMPLEMENTED_LIST:
				list_value = new ArrayList<PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template>(other_value.list_value.size());
				for(int i = 0; i < other_value.list_value.size(); i++) {
					final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template temp = new PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template(other_value.list_value.get(i));
					list_value.add(temp);
				}
				break;
			default:
				throw new TtcnError("Copying an uninitialized template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");
			}
			set_selection(other_value);
		}

		/**
		 * Matches the provided value against this template.
		 *
		 * @param other_value the value to be matched.
		 * */
		public boolean match(final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING other_value) {
			return match(other_value, false);
		}

		/**
		 * Matches the provided value against this template. In legacy mode
		 * omitted value fields are not matched against the template field.
		 *
		 * @param other_value
		 *                the value to be matched.
		 * @param legacy
		 *                use legacy mode.
		 * */
		public boolean match(final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING other_value, final boolean legacy) {
			if(!other_value.is_bound()) {
				return false;
			}
			final int value_length = other_value.size_of().get_int();
			if (!match_length(value_length)) {
				return false;
			}
			switch (template_selection) {
			case ANY_VALUE:
			case ANY_OR_OMIT:
				return true;
			case OMIT_VALUE:
				return false;
			case SPECIFIC_VALUE:
				return RecordOf_Match.match_record_of(other_value, value_length, this, value_elements.size(), match_function_specific, legacy);
			case VALUE_LIST:
			case COMPLEMENTED_LIST:
				for(int i = 0 ; i < list_value.size(); i++) {
					if(list_value.get(i).match(other_value, legacy)) {
						return template_selection == template_sel.VALUE_LIST;
					}
				}
				return template_selection == template_sel.COMPLEMENTED_LIST;
			default:
				throw new TtcnError("Matching with an uninitialized/unsupported template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");
			}
		}

		private boolean match_index(final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING value_ptr, final int value_index, final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template template_ptr, final int template_index, final boolean legacy) {
			if (value_index >= 0) {
				return template_ptr.value_elements.get(template_index).match(value_ptr.valueElements.get(value_index), legacy);
			} else {
				return template_ptr.value_elements.get(template_index).is_any_or_omit();
			}
		}

		@Override
		public boolean match(final Base_Type otherValue, final boolean legacy) {
			if (otherValue instanceof PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING) {
				return match((PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING)otherValue, legacy);
			}

			throw new TtcnError("Internal Error: The left operand of assignment is not of type PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING.");
		}

		@Override
		public boolean match_omit(final boolean legacy) {
			if (is_ifPresent) {
				return true;
			}
			switch (template_selection) {
			case OMIT_VALUE:
			case ANY_OR_OMIT:
				return true;
			case VALUE_LIST:
			case COMPLEMENTED_LIST:
				if (legacy) {
					for (int i = 0 ; i < list_value.size(); i++) {
						if (list_value.get(i).match_omit(legacy)) {
							return template_selection == template_sel.VALUE_LIST;
						}
					}
					return template_selection == template_sel.COMPLEMENTED_LIST;
				}
				return false;
			default:
				return false;
			}
		}

		@Override
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template operator_assign( final template_sel otherValue ) {
			check_single_selection(otherValue);
			clean_up();
			set_selection(otherValue);
			return this;
		}

		/**
		 * Assigns the other value to this template.
		 * Overwriting the current content in the process.
		 *<p>
		 * operator= in the core.
		 *
		 * @param otherValue
		 *                the other value to assign.
		 * @return the new template object.
		 */
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template operator_assign( final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING otherValue ) {
			clean_up();
			copy_value(otherValue);
			return this;
		}

		/**
		 * Assigns the other template to this template.
		 * Overwriting the current content in the process.
		 *<p>
		 * operator= in the core.
		 *
		 * @param otherValue
		 *                the other value to assign.
		 * @return the new template object.
		 */
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template operator_assign( final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template otherValue ) {
			if (otherValue != this) {
				clean_up();
				copy_template(otherValue);
			}
			return this;
		}

		@Override
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template operator_assign(final Base_Type otherValue) {
			if (otherValue instanceof PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING) {
				return operator_assign((PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING)otherValue);
			}

			throw new TtcnError("Internal Error: The left operand of assignment is not of type PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING.");
		}

		@Override
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template operator_assign(final Base_Template otherValue) {
			if (otherValue instanceof PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template) {
				return operator_assign((PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template)otherValue);
			}

			throw new TtcnError("Internal Error: The left operand of assignment is not of type PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template.");
		}

		/**
		 * Assigns the other value to this template.
		 * Overwriting the current content in the process.
		 *<p>
		 * operator= in the core.
		 *
		 * @param otherValue
		 *                the other value to assign.
		 * @return the new template object.
		 */
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template operator_assign( final Optional<PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING> other_value ) {
			clean_up();
			switch (other_value.get_selection()) {
			case OPTIONAL_PRESENT:
				copy_value(other_value.constGet());
				break;
			case OPTIONAL_OMIT:
				set_selection(template_sel.OMIT_VALUE);
				break;
			default:
				throw new TtcnError("Assignment of an unbound optional field to a template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");
			}
			return this;
		}
		/**
		 * Sets the current template to empty.
		 * Overwriting the current content in the process.
		 *<p>
		 * operator= in the core.
		 *
		 * @param nullValue
		 *                the null value.
		 * @return the new template object.
		 */
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template operator_assign(final TitanNull_Type nullValue) {
			clean_up();
			set_selection(template_sel.SPECIFIC_VALUE);
			value_elements = new ArrayList<TitanUniversalCharString_template>();
			return this;
		}


		@Override
		public void clean_up() {
			switch (template_selection) {
			case SPECIFIC_VALUE:
				value_elements.clear();
				value_elements = null;
				break;
			case VALUE_LIST:
			case COMPLEMENTED_LIST:
				list_value.clear();
				list_value = null;
				break;
			default:
				break;
			}
			template_selection = template_sel.UNINITIALIZED_TEMPLATE;
		}

		/**
		 * Creates a new record/set of value from the current value,
		 * with the parts from the provided index at the provided length
		 * being replaced by the provided values.
		 *
		 * @param index
		 *                the index to start replacing at.
		 * @param len
		 *                the number of elements to replace.
		 * @param repl
		 *                the values to insert.
		 * @return the new value.
		 * */
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING replace(final int index, final int len, final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template repl) {
			if (!is_value()) {
				throw new TtcnError("The first argument of function replace() is a template with non-specific value.");
			}
			if (!repl.is_value()) {
				throw new TtcnError("The fourth argument of function replace() is a template with non-specific value.");
			}
			return valueof().replace(index, len, repl.valueof());
		}

		/**
		 * Creates a new record/set of value from the current value,
		 * with the parts from the provided index at the provided length
		 * being replaced by the provided values.
		 *
		 * @param index
		 *                the index to start replacing at.
		 * @param len
		 *                the number of elements to replace.
		 * @param repl
		 *                the values to insert.
		 * @return the new value.
		 * */
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING replace(final TitanInteger index, final TitanInteger len, final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template repl) {
			if (!is_value()) {
				throw new TtcnError("The first argument of function replace() is a template with non-specific value.");
			}
			if (!repl.is_value()) {
				throw new TtcnError("The fourth argument of function replace() is a template with non-specific value.");
			}
			return valueof().replace(index.get_int(), len.get_int(), repl.valueof());
		}

		/**
		 * Creates a new record/set of value from the current value,
		 * with the parts from the provided index at the provided length
		 * being replaced by the provided values.
		 *
		 * @param index
		 *                the index to start replacing at.
		 * @param len
		 *                the number of elements to replace.
		 * @param repl
		 *                the values to insert.
		 * @return the new value.
		 * */
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING replace(final int index, final int len, final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING repl) {
			if (!is_value()) {
				throw new TtcnError("The first argument of function replace() is a template with non-specific value.");
			}
			return valueof().replace(index, len, repl);
		}

		/**
		 * Creates a new record/set of value from the current value,
		 * with the parts from the provided index at the provided length
		 * being replaced by the provided values.
		 *
		 * @param index
		 *                the index to start replacing at.
		 * @param len
		 *                the number of elements to replace.
		 * @param repl
		 *                the values to insert.
		 * @return the new value.
		 * */
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING replace(final TitanInteger index, final TitanInteger len, final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING repl) {
			if (!is_value()) {
				throw new TtcnError("The first argument of function replace() is a template with non-specific value.");
			}
			return valueof().replace(index.get_int(), len.get_int(), repl);
		}

		/**
		 * Gives access to the given element. Indexing begins from zero. If this
		 * element of the variable was never used before, new (unbound) elements
		 * will be allocated up to (and including) this index.
		 *
		 * Index underflow and overflow causes dynamic test case error.
		 * Also if the template is not a specific value template.
		 *
		 * operator[] in the core.
		 *
		 * @param index_value
		 *            the index of the element to return.
		 * @return the element at the specified position in this list
		 * */
		public TitanUniversalCharString_template get_at(final int index_value) {
			if (index_value < 0) {
				throw new TtcnError( MessageFormat.format( "Accessing an element of a template for type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING using a negative index: {0}.", index_value ) );
			}

			switch (template_selection) {
			case SPECIFIC_VALUE:
				if(index_value < value_elements.size()) {

					break;
				}
				// no break
			case OMIT_VALUE:
			case ANY_VALUE:
			case ANY_OR_OMIT:
			case UNINITIALIZED_TEMPLATE:
				set_size(index_value + 1);
				break;
			default:
				throw new TtcnError("Accessing an element of a non-specific template for type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");
			}
			return value_elements.get(index_value);
		}

		/**
		 * Gives access to the given element. Indexing begins from zero. If this
		 * element of the variable was never used before, new (unbound) elements
		 * will be allocated up to (and including) this index.
		 *
		 * Index underflow and overflow causes dynamic test case error.
		 * Also if the template is not a specific value template.
		 *
		 * operator[] in the core.
		 *
		 * @param index_value
		 *            the index of the element to return.
		 * @return the element at the specified position in this list
		 * */
		public TitanUniversalCharString_template get_at(final TitanInteger index_value) {
			index_value.must_bound("Using an unbound integer value for indexing a template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");

			return get_at(index_value.get_int());
		}

		/**
		 * Gives read-only access to the given element. Index underflow and overflow causes
		 * dynamic test case error. Also if the template is not a specific value template.
		 *
		 * const operator[] const in the core.
		 *
		 * @param index_value
		 *            the index of the element to return.
		 * @return the element at the specified position in this list
		 * */
		public TitanUniversalCharString_template constGet_at(final int index_value) {
			if (index_value < 0) {
				throw new TtcnError( MessageFormat.format( "Accessing an element of a template for type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING using a negative index: {0}.", index_value ) );
			}

			if (template_selection != template_sel.SPECIFIC_VALUE) {
				throw new TtcnError("Accessing an element of a non-specific template for type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");
			}

			if (index_value >= value_elements.size()) {
				throw new TtcnError( MessageFormat.format( "Index overflow in a template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING: The index is {0}, but the template has only {1} elements.", index_value, value_elements.size() ) );
			}

			return value_elements.get(index_value);
		}

		/**
		 * Gives read-only access to the given element. Index underflow and overflow causes
		 * dynamic test case error. Also if the template is not a specific value template.
		 *
		 * const operator[] const in the core.
		 *
		 * @param index_value
		 *            the index of the element to return.
		 * @return the element at the specified position in this list
		 * */
		public TitanUniversalCharString_template constGet_at(final TitanInteger index_value) {
			index_value.must_bound("Using an unbound integer value for indexing a template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");

			return constGet_at(index_value.get_int());
		}

		/**
		 * Sets the new size of the template.
		 * Also makes turns it into a specific value template if not already.
		 * If the new size is bigger than actual, unbound elements are added to the end.
		 * If the new size is smaller than actual, excess elements are removed.
		 *
		 * @param newSize the new size to be used.
		 * */
		public void set_size(final int new_size) {
			if (new_size < 0) {
				throw new TtcnError("Internal error: Setting a negative size for a template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");
			}
			final template_sel old_selection = template_selection;
			if (old_selection != template_sel.SPECIFIC_VALUE) {
				clean_up();
				set_selection(template_sel.SPECIFIC_VALUE);
				value_elements = null;
			}
			if (value_elements == null) {
				value_elements = new ArrayList<TitanUniversalCharString_template>(new_size);
			}
			if (new_size > value_elements.size()) {
				if (old_selection == template_sel.ANY_VALUE || old_selection == template_sel.ANY_OR_OMIT) {
					for (int elem_count = value_elements.size(); elem_count < new_size; elem_count++) {
						value_elements.add( new TitanUniversalCharString_template(template_sel.ANY_VALUE) );
					}
				} else {
					for (int elem_count = value_elements.size(); elem_count < new_size; elem_count++) {
						value_elements.add( new TitanUniversalCharString_template() );
					}
				}
			} else if (new_size < value_elements.size()) {
				while(value_elements.size() > new_size) {
					value_elements.remove(value_elements.size()-1);
				}
			}
		}

		/**
		 * Returns the number of elements.
		 * The value to be returned is the maximum of the minimal length restriction value of the type,
		 *  or 0 for types with no minimal length restriction,
		 *  and the index of the last initialized element plus 1.
		 *
		 * size_of in the core.
		 * deprecated by the standard.
		 *
		 * @return the number of elements.
		 * */
		public TitanInteger size_of() {
			return sizeOf(true);
		}

		/**
		 * Returns the number of elements, that is, the largest used index plus
		 * one and zero for the empty value.
		 *
		 * lengthof in the core
		 *
		 * @return the number of elements.
		 * */
		public TitanInteger lengthof() {
			return sizeOf(false);
		}

		/**
		 * A helper function to reduce code. Based on the parameter it
		 * can operate as size_of or lengthof.
		 *
		 * @param is_size
		 *                {@code true} to operate as size_of,
		 *                {@code false} otherwise.
		 * @return the appriopriate number based on the operation mode
		 *         selected.
		 * */
		public TitanInteger sizeOf(final boolean is_size) {
			final String op_name = is_size ? "size" : "length";
			if (is_ifPresent) {
				throw new TtcnError( MessageFormat.format( "Performing {0}of() operation on a template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING which has an ifpresent attribute.", op_name ) );
			}
			int min_size;
			boolean has_any_or_none;
			switch (template_selection)
			{
			case SPECIFIC_VALUE: {
				min_size = 0;
				has_any_or_none = false;
				int elem_count = value_elements.size();
				if (!is_size) {
					while (elem_count>0 && !(value_elements.get(elem_count-1)).is_bound()) {
						elem_count--;
					}
				}
				for (int i=0; i<elem_count; i++)
				{
					switch (value_elements.get(i).get_selection())
					{
					case OMIT_VALUE:
						throw new TtcnError( MessageFormat.format( "Performing {0}of() operation on a template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING containing omit element.", op_name ) );
					case ANY_OR_OMIT:
						has_any_or_none = true;
						break;
					default:
						min_size++;
						break;
					}
				}
			} break;
			case OMIT_VALUE:
				throw new TtcnError( MessageFormat.format( "Performing {0}of() operation on a template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING containing omit value.", op_name ) );
			case ANY_VALUE:
			case ANY_OR_OMIT:
				min_size = 0;
				has_any_or_none = true;
				break;
			case VALUE_LIST:
			{
				if (list_value.isEmpty()) {
					throw new TtcnError( MessageFormat.format( "Performing {0}of() operation on a template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING containing an empty list.", op_name ) );
				}
				final int item_size = list_value.get(0).sizeOf(is_size).get_int();
				for (int i = 1; i < list_value.size(); i++) {
					if (list_value.get(i).sizeOf(is_size).get_int()!=item_size) {
						throw new TtcnError( MessageFormat.format( "Performing {0}of() operation on a template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING containing a value list with different sizes.", op_name ) );
					}
				}
				min_size = item_size;
				has_any_or_none = false;
				break;
			}
			case COMPLEMENTED_LIST:
				throw new TtcnError( MessageFormat.format( "Performing {0}of() operation on a template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING containing complemented list.", op_name ) );
			default:
				throw new TtcnError( MessageFormat.format( "Performing {0}of() operation on an uninitialized/unsupported template of type PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING.", op_name ) );
			}
			return new TitanInteger(check_section_is_single(min_size, has_any_or_none, op_name, "a template of type", "TitanUniversalCharString_template"));
		}

		/**
		 * Returns the number of elements, that is, the largest used index plus
		 * one and zero for the empty value.
		 *
		 * n_elem in the core
		 *
		 * @return the number of elements.
		 * */
		public TitanInteger n_elem() {
			switch (template_selection) {
			case SPECIFIC_VALUE:
				return new TitanInteger(value_elements.size());
			case COMPLEMENTED_LIST:
				throw new TtcnError("Performing n_elem() operation on a template of type PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING containing complemented list.");
			case UNINITIALIZED_TEMPLATE:
			case OMIT_VALUE:
			case ANY_VALUE:
			case ANY_OR_OMIT:
			case VALUE_LIST:
			case VALUE_RANGE:
			case STRING_PATTERN:
			case SUPERSET_MATCH:
			case SUBSET_MATCH:
			case DECODE_MATCH:
				break;
			}
			throw new TtcnError("Performing n_elem() operation on an uninitialized/unsupported template of type PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING.");
		}

		@Override
		public boolean is_value() {
			if (template_selection != template_sel.SPECIFIC_VALUE || is_ifPresent) {
				return false;
			}
			for (int elem_count = 0; elem_count < value_elements.size(); elem_count++) {
				if (!value_elements.get(elem_count).is_value()) {
					return false;
				}
			}
			return true;
		}

		@Override
		public void set_type(final template_sel template_type, final int list_length) {
			clean_up();
			switch (template_type) {
			case VALUE_LIST:
			case COMPLEMENTED_LIST:
				list_value = new ArrayList<PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template>( list_length );
				for (int list_count = 0; list_count < list_length; list_count++) {
					list_value.add( new PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template() );
				}
				break;
			default:
				throw new TtcnError("Internal error: Setting an invalid type for a template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");
			}
			set_selection(template_type);
		}

		@Override
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template list_item(final int list_index) {
			if (template_selection != template_sel.VALUE_LIST && template_selection != template_sel.COMPLEMENTED_LIST) {
				throw new TtcnError("Accessing a list element of a non-list template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");
			}
			if (list_index < 0) {
				throw new TtcnError(MessageFormat.format("Internal error: Accessing a value list template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING using a negative index ({0}).", list_index));
			} else if (list_index >= list_value.size()) {
				throw new TtcnError("Index overflow in a value list template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");
			}
			return list_value.get(list_index);
		}

		/**
		 * Accessor for list items of value list and complemented list
		 * templates.
		 *
		 * Underflow and overflow results in dynamic testcase
		 * error. list_item in the core.
		 *
		 * @param list_index
		 *                the index of the list item.
		 * @return the list item at the provided index.
		 * */
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template get_list_item(final int list_index) {
			if (template_selection != template_sel.VALUE_LIST && template_selection != template_sel.COMPLEMENTED_LIST) {
				throw new TtcnError("Internal error: Accessing a list element of a non-list template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");
			}
			if (list_index < 0) {
				throw new TtcnError(MessageFormat.format("Internal error: Accessing a value list template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING using a negative index ({0}).", list_index));
			} else if (list_index >= list_value.size()) {
				throw new TtcnError("Internal error: Index overflow in a value list template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");
			}
			return list_value.get( list_index );
		}

		@Override
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING valueof() {
			if (template_selection != template_sel.SPECIFIC_VALUE || is_ifPresent) {
				throw new TtcnError("Performing a valueof or send operation on a non-specific template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");
			}
			final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING ret_val = new PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING(TitanNull_Type.NULL_VALUE);
			for (int elem_count = 0; elem_count < value_elements.size(); elem_count++) {
				if (value_elements.get(elem_count).is_bound()) {
					ret_val.valueElements.add( value_elements.get(elem_count).valueof() );
				}
			}
			return ret_val;
		}

		/**
		 * Creates a new record/set of value from the current value,
		 * with the elements from the provided index at the provided length.
		 *
		 * @param index
		 *                the index to start at.
		 * @param returncount
		 *                the number of elements to copy.
		 * @return the new value.
		 * */
		public PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING substr(final int index, final int returncount) {
			if (!is_value()) {
				throw new TtcnError("The first argument of function substr() is a template with non-specific value.");
			}
			return valueof().substr(index, returncount);
		}

		@Override
		public void log() {
			switch (template_selection) {
			case SPECIFIC_VALUE:
				if (value_elements.isEmpty()) {
					TTCN_Logger.log_event_str("{ }");
				} else {
					TTCN_Logger.log_event_str("{ ");
					for (int elem_count = 0; elem_count < value_elements.size(); elem_count++) {
						if (elem_count > 0) {
							TTCN_Logger.log_event_str(", ");
						}
						if (permutation_starts_at(elem_count)) {
							TTCN_Logger.log_event_str("permutation(");
						}
						value_elements.get(elem_count).log();
						if (permutation_ends_at(elem_count)) {
							TTCN_Logger.log_char(')');
						}
					}
					TTCN_Logger.log_event_str(" }");
				}
				break;
			case COMPLEMENTED_LIST:
				TTCN_Logger.log_event_str("complement");
			case VALUE_LIST:
				TTCN_Logger.log_char('(');
				for (int list_count = 0; list_count < list_value.size(); list_count++) {
					if (list_count > 0) {
						TTCN_Logger.log_event_str(", ");
					}
					list_value.get(list_count).log();
				}
				TTCN_Logger.log_char(')');
				break;
			default:
				log_generic();
			}
			log_restricted();
			log_ifpresent();
		}

		/**
		 * Logs the matching of the provided value to this template, to help
		 * identify the reason for mismatch.
		 *
		 * @param match_value
		 *                the value to be matched.
		 * */
		public void log_match(final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING match_value) {
			log_match(match_value, false);
		}

		@Override
		public void log_match(final Base_Type match_value, final boolean legacy) {
			if (match_value instanceof PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING) {
				log_match((PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING)match_value, legacy);
				return;
			}

			throw new TtcnError("Internal Error: value can not be cast to @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");
		}

		/**
		 * Logs the matching of the provided value to this template, to help
		 * identify the reason for mismatch. In legacy mode omitted value fields
		 * are not matched against the template field.
		 *
		 * @param match_value
		 *                the value to be matched.
		 * @param legacy
		 *                use legacy mode.
		 * */
		public void log_match(final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING match_value, final boolean legacy) {
			if ( TTCN_Logger.matching_verbosity_t.VERBOSITY_COMPACT == TTCN_Logger.get_matching_verbosity() ) {
				if(match(match_value, legacy)) {
					TTCN_Logger.print_logmatch_buffer();
					TTCN_Logger.log_event_str(" matched");
				} else {
					if (template_selection == template_sel.SPECIFIC_VALUE && !value_elements.isEmpty() && get_number_of_permutations() == 0 && value_elements.size() == match_value.size_of().get_int()) {
						final int previous_size = TTCN_Logger.get_logmatch_buffer_len();
						for (int elem_count = 0; elem_count < value_elements.size(); elem_count++) {
							if ( !value_elements.get(elem_count).match(match_value.constGet_at(elem_count), legacy) ) {
								TTCN_Logger.log_logmatch_info("[%d]", elem_count);
								value_elements.get(elem_count).log_match( match_value.constGet_at(elem_count), legacy );
								TTCN_Logger.set_logmatch_buffer_len(previous_size);
							}
						}
						log_match_length(value_elements.size());
					} else {
						TTCN_Logger.print_logmatch_buffer();
						match_value.log();
						TTCN_Logger.log_event_str(" with ");
						log();
						TTCN_Logger.log_event_str(" unmatched");
					}
				}
				return;
			}
			if (template_selection == template_sel.SPECIFIC_VALUE && !value_elements.isEmpty() && get_number_of_permutations() == 0 && value_elements.size() == match_value.size_of().get_int()) {
				TTCN_Logger.log_event_str("{ ");
				for (int elem_count = 0; elem_count < value_elements.size(); elem_count++) {
					if (elem_count > 0) {
						TTCN_Logger.log_event_str(", ");
					}
					value_elements.get(elem_count).log_match( match_value.constGet_at(elem_count), legacy );
				}
				TTCN_Logger.log_event_str(" }");
				log_match_length(value_elements.size());
			} else {
				match_value.log();
				TTCN_Logger.log_event_str(" with ");
				log();
				if ( match(match_value, legacy) ) {
					TTCN_Logger.log_event_str(" matched");
				} else {
					TTCN_Logger.log_event_str(" unmatched");
				}
			}
		}

		@Override
		public void encode_text(final Text_Buf text_buf) {
			encode_text_permutation(text_buf);
			switch (template_selection) {
			case OMIT_VALUE:
			case ANY_VALUE:
			case ANY_OR_OMIT:
				break;
			case SPECIFIC_VALUE:
				text_buf.push_int(value_elements.size());
				for (int i = 0; i < value_elements.size(); i++) {
					value_elements.get(i).encode_text(text_buf);
				}
				break;
			case VALUE_LIST:
			case COMPLEMENTED_LIST:
				text_buf.push_int(list_value.size());
				for (int i = 0; i < list_value.size(); i++) {
					list_value.get(i).encode_text(text_buf);
				}
				break;
			default:
				throw new TtcnError("Text encoder: Encoding an uninitialized/unsupported template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");
			}
		}

		@Override
		public void decode_text(final Text_Buf text_buf) {
			clean_up();
			decode_text_permutation(text_buf);
			switch (template_selection) {
			case OMIT_VALUE:
			case ANY_VALUE:
			case ANY_OR_OMIT:
				break;
			case SPECIFIC_VALUE: {
				final int temp = text_buf.pull_int().get_int();
				if (temp < 0) {
					throw new TtcnError("Text decoder: Negative size was received for a template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");
				}
				value_elements = new ArrayList<TitanUniversalCharString_template>(temp);
				for (int i = 0; i < temp; i++) {
					final TitanUniversalCharString_template temp2 = new TitanUniversalCharString_template();
					temp2.decode_text(text_buf);
					value_elements.add(temp2);
				}
				break;
			}
			case VALUE_LIST:
			case COMPLEMENTED_LIST: {
				final int size = text_buf.pull_int().get_int();
				list_value = new ArrayList<PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template>(size);
				for (int i = 0; i < size; i++) {
					final PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template temp2 = new PREGEN__RECORD__OF__UNIVERSAL__CHARSTRING_template();
					temp2.decode_text(text_buf);
					list_value.add(temp2);
				}
				break;
			}
			default:
				throw new TtcnError("Text decoder: An unknown/unsupported selection was received for a template of type @PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING.");
			}
		}

		@Override
		public void set_param(final Module_Parameter param) {
			param.basic_check(Module_Parameter.basic_check_bits_t.BC_TEMPLATE.getValue(), "record of template");
			switch (param.get_type()) {
			case MP_Omit:
				operator_assign(template_sel.OMIT_VALUE);
				break;
			case MP_Any:
				operator_assign(template_sel.ANY_VALUE);
				break;
			case MP_AnyOrNone:
				operator_assign(template_sel.ANY_OR_OMIT);
				break;
			case MP_List_Template:
			case MP_ComplementList_Template: {
				final int size = param.get_size();
				set_type(param.get_type() == Module_Parameter.type_t.MP_List_Template ? template_sel.VALUE_LIST : template_sel.COMPLEMENTED_LIST, size);
				for (int i = 0; i < size; i++) {
					list_item(i).set_param(param.get_elem(i));
				}
				break;
			}
			case MP_Indexed_List:
				if (template_selection != template_sel.SPECIFIC_VALUE) {
					set_size(0);
				}
				for (int i = 0; i < param.get_size(); i++) {
					get_at(param.get_elem(i).get_id().get_index()).set_param(param.get_elem(i));
				}
				break;
			case MP_Value_List: {
				set_size(param.get_size());
				int current_index = 0;
				for (int i = 0; i < param.get_size(); i++) {
					switch (param.get_elem(i).get_type()) {
					case MP_NotUsed:
						current_index++;
						break;
					case MP_Permutation_Template: {
						final int permutation_start_index = current_index;
						final Module_Parameter param_i = param.get_elem(i);
						for (int perm_i = 0; perm_i < param_i.get_size(); perm_i++) {
							get_at(current_index).set_param(param_i.get_elem(perm_i));
							current_index++;
						}
						final int permutation_end_index = current_index - 1;
						add_permutation(permutation_start_index, permutation_end_index);
						break;
					}
					default:
						get_at(current_index).set_param(param.get_elem(i));
						current_index++;
						break;
					}
				}
				break;
			}
			default:
				param.type_error("record of template", "@PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING");
				break;
			}
			is_ifPresent = param.get_ifpresent();
			set_length_range(param);
		}

		@Override
		public boolean get_istemplate_kind(final String type) {
			if ("AnyElement".equals(type)) {
				if (template_selection != template_sel.SPECIFIC_VALUE) {
					return false;
				}
				for (int i = 0; i < value_elements.size(); i++) {
					if (value_elements.get(i).get_selection() == template_sel.ANY_VALUE) {
						return true;
					}
				}
				return false;
			} else if ("AnyElementsOrNone".equals(type)) {
				if (template_selection != template_sel.SPECIFIC_VALUE) {
					return false;
				}
				for (int i = 0; i < value_elements.size(); i++) {
					if (value_elements.get(i).get_selection() == template_sel.ANY_OR_OMIT) {
						return true;
					}
				}
				return false;
			} else if ("permutation".equals(type)) {
				return get_number_of_permutations() != 0;
			} else if ("length".equals(type)) {
				return length_restriction_type != length_restriction_type_t.NO_LENGTH_RESTRICTION;
			} else {
				return super.get_istemplate_kind(type);
			}
		}

		@Override
		public void check_restriction(final template_res restriction, final String name, final boolean legacy) {
			if (template_selection==template_sel.UNINITIALIZED_TEMPLATE) {
				return;
			}
			switch ((name != null && (restriction==template_res.TR_VALUE)) ? template_res.TR_OMIT : restriction) {
			case TR_OMIT:
				if (template_selection==template_sel.OMIT_VALUE) {
					return;
				}
				// no break
			case TR_VALUE:
				if (template_selection!=template_sel.SPECIFIC_VALUE || is_ifPresent) {
					break;
				}
				for (int i=0; i<value_elements.size(); i++) {
					value_elements.get(i).check_restriction(restriction, name == null ? "@PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING" : name, false);
				}
				return;
			case TR_PRESENT:
				if (!match_omit(legacy)) {
					return;
				}
				break;
			default:
				return;
			}
			throw new TtcnError(MessageFormat.format("Restriction `{0}'' on template of type {1} violated.", get_res_name(restriction), name == null ? "@PreGenRecordOf.PREGEN_RECORD_OF_UNIVERSAL_CHARSTRING" : name));
		}
	}