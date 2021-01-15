	public static class Port__Queue_template extends Base_Template {
		private Port__Queue_operation_template operation; //TTCN3_Enumerated_Type
		private TitanCharString_template port__name; //CharString_Type
		private TitanInteger_template compref; //Integer_Type
		private TitanInteger_template msgid; //Integer_Type
		private TitanCharString_template address__; //CharString_Type
		private TitanCharString_template param__; //CharString_Type
		//originally value_list/list_value
		private List<Port__Queue_template> list_value;


		/**
		 * Initializes to unbound/uninitialized template.
		 * */
		public Port__Queue_template() {
			// do nothing
		}

		/**
		 * Initializes to a given template kind.
		 *
		 * @param otherValue
		 *                the template kind to initialize to.
		 * */
		public Port__Queue_template(final template_sel otherValue ) {
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
		public Port__Queue_template( final Port__Queue otherValue ) {
			copy_value(otherValue);
		}

		/**
		 * Initializes to a given template.
		 * The elements of the provided template are copied.
		 *
		 * @param otherValue
		 *                the value to initialize to.
		 * */
		public Port__Queue_template( final Port__Queue_template otherValue ) {
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
		public Port__Queue_template( final Optional<Port__Queue> otherValue ) {
			switch (otherValue.get_selection()) {
			case OPTIONAL_PRESENT:
				copy_value(otherValue.constGet());
				break;
			case OPTIONAL_OMIT:
				set_selection(template_sel.OMIT_VALUE);
				break;
			default:
				throw new TtcnError("Creating a template of type @TitanLoggerApi.Port_Queue from an unbound optional field.");
			}
		}

		@Override
		public Port__Queue_template operator_assign( final template_sel otherValue ) {
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
		public Port__Queue_template operator_assign( final Port__Queue otherValue ) {
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
		public Port__Queue_template operator_assign( final Port__Queue_template otherValue ) {
			if (otherValue != this) {
				clean_up();
				copy_template(otherValue);
			}
			return this;
		}

		@Override
		public Port__Queue_template operator_assign(final Base_Type otherValue) {
			if (otherValue instanceof Port__Queue) {
				return operator_assign((Port__Queue) otherValue);
			}

			throw new TtcnError(MessageFormat.format("Internal Error: value `Port__Queue' can not be cast to {1}", otherValue));
		}

		@Override
		public Port__Queue_template operator_assign(final Base_Template otherValue) {
			if (otherValue instanceof Port__Queue_template) {
				return operator_assign((Port__Queue_template) otherValue);
			}

			throw new TtcnError(MessageFormat.format("Internal Error: value `Port__Queue' can not be cast to {1}_template", otherValue));
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
		public Port__Queue_template operator_assign( final Optional<Port__Queue> otherValue ) {
			clean_up();
			switch (otherValue.get_selection()) {
			case OPTIONAL_PRESENT:
				copy_value(otherValue.constGet());
				break;
			case OPTIONAL_OMIT:
				set_selection(template_sel.OMIT_VALUE);
				break;
			default:
				throw new TtcnError("Assignment of an unbound optional field to a template of type @TitanLoggerApi.Port_Queue.");
			}
			return this;
		}

		/**
		 * Internal function to copy the provided value into this template.
		 * The template becomes a specific value template.
		 * The already existing content is overwritten.
		 *
		 * @param other_value the value to be copied.
		 * */
		private void copy_value(final Port__Queue other_value) {
			if (other_value.get_field_operation().is_bound()) {
				get_field_operation().operator_assign(other_value.get_field_operation());
			} else {
				get_field_operation().clean_up();
			}
			if (other_value.get_field_port__name().is_bound()) {
				get_field_port__name().operator_assign(other_value.get_field_port__name());
			} else {
				get_field_port__name().clean_up();
			}
			if (other_value.get_field_compref().is_bound()) {
				get_field_compref().operator_assign(other_value.get_field_compref());
			} else {
				get_field_compref().clean_up();
			}
			if (other_value.get_field_msgid().is_bound()) {
				get_field_msgid().operator_assign(other_value.get_field_msgid());
			} else {
				get_field_msgid().clean_up();
			}
			if (other_value.get_field_address__().is_bound()) {
				get_field_address__().operator_assign(other_value.get_field_address__());
			} else {
				get_field_address__().clean_up();
			}
			if (other_value.get_field_param__().is_bound()) {
				get_field_param__().operator_assign(other_value.get_field_param__());
			} else {
				get_field_param__().clean_up();
			}
			set_selection(template_sel.SPECIFIC_VALUE);
		}

		/**
		 * Internal function to copy the provided template into this template.
		 * The already existing content is overwritten.
		 *
		 * @param other_value the value to be copied.
		 * */
		private void copy_template(final Port__Queue_template other_value) {
			switch (other_value.template_selection) {
			case SPECIFIC_VALUE:
				if (template_sel.UNINITIALIZED_TEMPLATE == other_value.get_field_operation().get_selection()) {
					get_field_operation().clean_up();
				} else {
					get_field_operation().operator_assign(other_value.get_field_operation());
				}
				if (template_sel.UNINITIALIZED_TEMPLATE == other_value.get_field_port__name().get_selection()) {
					get_field_port__name().clean_up();
				} else {
					get_field_port__name().operator_assign(other_value.get_field_port__name());
				}
				if (template_sel.UNINITIALIZED_TEMPLATE == other_value.get_field_compref().get_selection()) {
					get_field_compref().clean_up();
				} else {
					get_field_compref().operator_assign(other_value.get_field_compref());
				}
				if (template_sel.UNINITIALIZED_TEMPLATE == other_value.get_field_msgid().get_selection()) {
					get_field_msgid().clean_up();
				} else {
					get_field_msgid().operator_assign(other_value.get_field_msgid());
				}
				if (template_sel.UNINITIALIZED_TEMPLATE == other_value.get_field_address__().get_selection()) {
					get_field_address__().clean_up();
				} else {
					get_field_address__().operator_assign(other_value.get_field_address__());
				}
				if (template_sel.UNINITIALIZED_TEMPLATE == other_value.get_field_param__().get_selection()) {
					get_field_param__().clean_up();
				} else {
					get_field_param__().operator_assign(other_value.get_field_param__());
				}
				break;
			case OMIT_VALUE:
			case ANY_VALUE:
			case ANY_OR_OMIT:
				break;
			case VALUE_LIST:
			case COMPLEMENTED_LIST:
				list_value = new ArrayList<Port__Queue_template>(other_value.list_value.size());
				for(int i = 0; i < other_value.list_value.size(); i++) {
					final Port__Queue_template temp = new Port__Queue_template(other_value.list_value.get(i));
					list_value.add(temp);
				}
				break;
			default:
				throw new TtcnError("Copying an uninitialized template of type @TitanLoggerApi.Port_Queue.");
			}
			set_selection(other_value);
		}

		@Override
		public void set_type(final template_sel template_type, final int list_length) {
			if (template_type != template_sel.VALUE_LIST && template_type != template_sel.COMPLEMENTED_LIST) {
				throw new TtcnError("Setting an invalid list for a template of type @TitanLoggerApi.Port_Queue.");
			}
			clean_up();
			set_selection(template_type);
			list_value = new ArrayList<Port__Queue_template>(list_length);
			for(int i = 0 ; i < list_length; i++) {
				list_value.add(new Port__Queue_template());
			}
		}


		@Override
		public boolean is_bound() {
			if (template_selection == template_sel.UNINITIALIZED_TEMPLATE && !is_ifPresent) {
				return false;
			}
			if (template_selection != template_sel.SPECIFIC_VALUE) {
				return true;
			}
			return operation.is_bound()
					|| port__name.is_bound()
					|| compref.is_bound()
					|| msgid.is_bound()
					|| address__.is_bound()
					|| param__.is_bound();
		}

		@Override
		public boolean is_present(final boolean legacy) {
			return is_present_(legacy);
		}

		private boolean is_present_(final boolean legacy) {
			if (template_selection==template_sel.UNINITIALIZED_TEMPLATE) {
				return false;
			}
			return !match_omit_(legacy);
		}

		@Override
		public boolean match_omit(final boolean legacy) {
			return match_omit_(legacy);
		}

		private boolean match_omit_(final boolean legacy) {
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
					for (int l_idx=0; l_idx<list_value.size(); l_idx++) {
						if (list_value.get(l_idx).match_omit_(legacy)) {
							return template_selection==template_sel.VALUE_LIST;
						}
					}
					return template_selection==template_sel.COMPLEMENTED_LIST;
				} // else fall through
			default:
				return false;
			}
		}

		@Override
		public boolean is_value() {
			if (template_selection != template_sel.SPECIFIC_VALUE || is_ifPresent) {
				return false;
			}
			return operation.is_value()
					&& port__name.is_value()
					&& compref.is_value()
					&& msgid.is_value()
					&& address__.is_value()
					&& param__.is_value();
		}
		/**
		 * Gives access to the field operation.
		 * Turning the template into a specific value template if needed.
		 *
		 * @return the field operation.
		 * */
		public Port__Queue_operation_template get_field_operation() {
			set_specific();
			return operation;
		}

		/**
		 * Gives read-only access to the field operation.
		 * Being called on a non specific value template causes dynamic test case error.
		 *
		 * @return the field operation.
		 * */
		public Port__Queue_operation_template constGet_field_operation() {
			if (template_selection != template_sel.SPECIFIC_VALUE) {
				throw new TtcnError("Accessing field operation of a non-specific template of type @TitanLoggerApi.Port_Queue.");
			}
			return operation;
		}

		/**
		 * Gives access to the field port_name.
		 * Turning the template into a specific value template if needed.
		 *
		 * @return the field port_name.
		 * */
		public TitanCharString_template get_field_port__name() {
			set_specific();
			return port__name;
		}

		/**
		 * Gives read-only access to the field port_name.
		 * Being called on a non specific value template causes dynamic test case error.
		 *
		 * @return the field port_name.
		 * */
		public TitanCharString_template constGet_field_port__name() {
			if (template_selection != template_sel.SPECIFIC_VALUE) {
				throw new TtcnError("Accessing field port_name of a non-specific template of type @TitanLoggerApi.Port_Queue.");
			}
			return port__name;
		}

		/**
		 * Gives access to the field compref.
		 * Turning the template into a specific value template if needed.
		 *
		 * @return the field compref.
		 * */
		public TitanInteger_template get_field_compref() {
			set_specific();
			return compref;
		}

		/**
		 * Gives read-only access to the field compref.
		 * Being called on a non specific value template causes dynamic test case error.
		 *
		 * @return the field compref.
		 * */
		public TitanInteger_template constGet_field_compref() {
			if (template_selection != template_sel.SPECIFIC_VALUE) {
				throw new TtcnError("Accessing field compref of a non-specific template of type @TitanLoggerApi.Port_Queue.");
			}
			return compref;
		}

		/**
		 * Gives access to the field msgid.
		 * Turning the template into a specific value template if needed.
		 *
		 * @return the field msgid.
		 * */
		public TitanInteger_template get_field_msgid() {
			set_specific();
			return msgid;
		}

		/**
		 * Gives read-only access to the field msgid.
		 * Being called on a non specific value template causes dynamic test case error.
		 *
		 * @return the field msgid.
		 * */
		public TitanInteger_template constGet_field_msgid() {
			if (template_selection != template_sel.SPECIFIC_VALUE) {
				throw new TtcnError("Accessing field msgid of a non-specific template of type @TitanLoggerApi.Port_Queue.");
			}
			return msgid;
		}

		/**
		 * Gives access to the field address_.
		 * Turning the template into a specific value template if needed.
		 *
		 * @return the field address_.
		 * */
		public TitanCharString_template get_field_address__() {
			set_specific();
			return address__;
		}

		/**
		 * Gives read-only access to the field address_.
		 * Being called on a non specific value template causes dynamic test case error.
		 *
		 * @return the field address_.
		 * */
		public TitanCharString_template constGet_field_address__() {
			if (template_selection != template_sel.SPECIFIC_VALUE) {
				throw new TtcnError("Accessing field address_ of a non-specific template of type @TitanLoggerApi.Port_Queue.");
			}
			return address__;
		}

		/**
		 * Gives access to the field param_.
		 * Turning the template into a specific value template if needed.
		 *
		 * @return the field param_.
		 * */
		public TitanCharString_template get_field_param__() {
			set_specific();
			return param__;
		}

		/**
		 * Gives read-only access to the field param_.
		 * Being called on a non specific value template causes dynamic test case error.
		 *
		 * @return the field param_.
		 * */
		public TitanCharString_template constGet_field_param__() {
			if (template_selection != template_sel.SPECIFIC_VALUE) {
				throw new TtcnError("Accessing field param_ of a non-specific template of type @TitanLoggerApi.Port_Queue.");
			}
			return param__;
		}

		private void set_specific() {
			if (template_selection != template_sel.SPECIFIC_VALUE) {
				final template_sel old_selection = template_selection;
				clean_up();
				set_selection(template_sel.SPECIFIC_VALUE);
				if (old_selection == template_sel.ANY_VALUE || old_selection == template_sel.ANY_OR_OMIT) {
					operation = new Port__Queue_operation_template(template_sel.ANY_VALUE);
					port__name = new TitanCharString_template(template_sel.ANY_VALUE);
					compref = new TitanInteger_template(template_sel.ANY_VALUE);
					msgid = new TitanInteger_template(template_sel.ANY_VALUE);
					address__ = new TitanCharString_template(template_sel.ANY_VALUE);
					param__ = new TitanCharString_template(template_sel.ANY_VALUE);
				} else {
					operation = new Port__Queue_operation_template();
					port__name = new TitanCharString_template();
					compref = new TitanInteger_template();
					msgid = new TitanInteger_template();
					address__ = new TitanCharString_template();
					param__ = new TitanCharString_template();
				}
			}
		}
		/**
		 * Matches the provided value against this template.
		 *
		 * @param other_value the value to be matched.
		 * */
		public boolean match(final Port__Queue other_value) {
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
		public boolean match(final Port__Queue other_value, final boolean legacy) {
			if (!other_value.is_bound()) {
				return false;
			}
			switch (template_selection) {
			case ANY_VALUE:
			case ANY_OR_OMIT:
				return true;
			case OMIT_VALUE:
				return false;
			case SPECIFIC_VALUE:
				if(!other_value.get_field_operation().is_bound()) {
					return false;
				}
				if(!operation.match(other_value.get_field_operation(), legacy)) {
					return false;
				}
				if(!other_value.get_field_port__name().is_bound()) {
					return false;
				}
				if(!port__name.match(other_value.get_field_port__name(), legacy)) {
					return false;
				}
				if(!other_value.get_field_compref().is_bound()) {
					return false;
				}
				if(!compref.match(other_value.get_field_compref(), legacy)) {
					return false;
				}
				if(!other_value.get_field_msgid().is_bound()) {
					return false;
				}
				if(!msgid.match(other_value.get_field_msgid(), legacy)) {
					return false;
				}
				if(!other_value.get_field_address__().is_bound()) {
					return false;
				}
				if(!address__.match(other_value.get_field_address__(), legacy)) {
					return false;
				}
				if(!other_value.get_field_param__().is_bound()) {
					return false;
				}
				if(!param__.match(other_value.get_field_param__(), legacy)) {
					return false;
				}
				return true;
			case VALUE_LIST:
			case COMPLEMENTED_LIST:
				for (int list_count = 0; list_count < list_value.size(); list_count++) {
					if (list_value.get(list_count).match(other_value, legacy)) {
						return template_selection == template_sel.VALUE_LIST;
					}
				}
				return template_selection == template_sel.COMPLEMENTED_LIST;
			default:
				throw new TtcnError("Matching an uninitialized/unsupported template of type @TitanLoggerApi.Port_Queue.");
			}
		}


		@Override
		public boolean match(final Base_Type otherValue, final boolean legacy) {
			if (otherValue instanceof Port__Queue) {
				return match((Port__Queue)otherValue, legacy);
			}

			throw new TtcnError("Internal Error: The left operand of assignment is not of type Port__Queue.");
		}


		@Override
		public Port__Queue valueof() {
			if (template_selection != template_sel.SPECIFIC_VALUE || is_ifPresent) {
				throw new TtcnError("Performing a valueof or send operation on a non-specific template of type @TitanLoggerApi.Port_Queue.");
			}
			final Port__Queue ret_val = new Port__Queue();
			if (operation.is_bound()) {
				ret_val.get_field_operation().operator_assign(operation.valueof());
			}
			if (port__name.is_bound()) {
				ret_val.get_field_port__name().operator_assign(port__name.valueof());
			}
			if (compref.is_bound()) {
				ret_val.get_field_compref().operator_assign(compref.valueof());
			}
			if (msgid.is_bound()) {
				ret_val.get_field_msgid().operator_assign(msgid.valueof());
			}
			if (address__.is_bound()) {
				ret_val.get_field_address__().operator_assign(address__.valueof());
			}
			if (param__.is_bound()) {
				ret_val.get_field_param__().operator_assign(param__.valueof());
			}
			return ret_val;
		}

		/**
		 * Returns the size (number of fields).
		 *
		 * size_of in the core
		 *
		 * @return the size of the structure.
		 * */
		public TitanInteger size_of() {
			if (is_ifPresent) {
				throw new TtcnError("Performing sizeof() operation on a template of type @TitanLoggerApi.Port_Queue which has an ifpresent attribute.");
			}
			switch (template_selection) {
			case SPECIFIC_VALUE:
				return new TitanInteger(6);
			case VALUE_LIST:
				if (list_value.isEmpty()) {
					throw new TtcnError("Internal error: Performing sizeof() operation on a template of type @TitanLoggerApi.Port_Queue containing an empty list.");
				}
				final int item_size = list_value.get(0).size_of().get_int();
				for (int l_idx = 1; l_idx < list_value.size(); l_idx++) {
					if (list_value.get(l_idx).size_of().get_int() != item_size) {
						throw new TtcnError("Performing sizeof() operation on a template of type @TitanLoggerApi.Port_Queue containing a value list with different sizes.");
					}
				}
				return new TitanInteger(item_size);
			case OMIT_VALUE:
				throw new TtcnError("Performing sizeof() operation on a template of type @TitanLoggerApi.Port_Queue containing omit value.");
			case ANY_VALUE:
			case ANY_OR_OMIT:
				throw new TtcnError("Performing sizeof() operation on a template of type @TitanLoggerApi.Port_Queue containing */? value.");
			case COMPLEMENTED_LIST:
				throw new TtcnError("Performing sizeof() operation on a template of type @TitanLoggerApi.Port_Queue containing complemented list.");
			default:
				throw new TtcnError("Performing sizeof() operation on an uninitialized/unsupported template of type @TitanLoggerApi.Port_Queue.");
			}
		}

		@Override
		public Port__Queue_template list_item(final int list_index) {
			if (template_selection != template_sel.VALUE_LIST && template_selection != template_sel.COMPLEMENTED_LIST) {
				throw new TtcnError("Accessing a list element of a non-list template of type @TitanLoggerApi.Port_Queue.");
			}
			if (list_index < 0) {
				throw new TtcnError(MessageFormat.format("Internal error: Accessing a value list template of type @TitanLoggerApi.Port_Queue using a negative index ({0}).", list_index));
			} else if (list_index >= list_value.size()) {
				throw new TtcnError("Index overflow in a value list template of type @TitanLoggerApi.Port_Queue.");
			}
			return list_value.get(list_index);
		}

		@Override
		public void log() {
			switch (template_selection) {
			case SPECIFIC_VALUE:
				TTCN_Logger.log_char('{');
				TTCN_Logger.log_event_str(" operation := ");
				operation.log();
				TTCN_Logger.log_char(',');
				TTCN_Logger.log_event_str(" port_name := ");
				port__name.log();
				TTCN_Logger.log_char(',');
				TTCN_Logger.log_event_str(" compref := ");
				compref.log();
				TTCN_Logger.log_char(',');
				TTCN_Logger.log_event_str(" msgid := ");
				msgid.log();
				TTCN_Logger.log_char(',');
				TTCN_Logger.log_event_str(" address_ := ");
				address__.log();
				TTCN_Logger.log_char(',');
				TTCN_Logger.log_event_str(" param_ := ");
				param__.log();
				TTCN_Logger.log_event_str(" }");
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
				break;
			}
			log_ifpresent();
		}

		/**
		 * Logs the matching of the provided value to this template, to help
		 * identify the reason for mismatch.
		 *
		 * @param match_value
		 *                the value to be matched.
		 * */
		public void log_match(final Port__Queue match_value) {
			log_match(match_value, false);
		}

		@Override
		public void log_match(final Base_Type match_value, final boolean legacy) {
			if (match_value instanceof Port__Queue) {
				log_match((Port__Queue)match_value, legacy);
				return;
			}

			throw new TtcnError("Internal Error: value can not be cast to @TitanLoggerApi.Port_Queue.");
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
		public void log_match(final Port__Queue match_value, final boolean legacy) {
			if ( TTCN_Logger.matching_verbosity_t.VERBOSITY_COMPACT == TTCN_Logger.get_matching_verbosity() ) {
				if(match(match_value, legacy)) {
					TTCN_Logger.print_logmatch_buffer();
					TTCN_Logger.log_event_str(" matched");
				} else {
					if (template_selection == template_sel.SPECIFIC_VALUE) {
						final int previous_size = TTCN_Logger.get_logmatch_buffer_len();
						if( !operation.match(match_value.constGet_field_operation(), legacy) ) {
							TTCN_Logger.log_logmatch_info(".operation");
							operation.log_match(match_value.constGet_field_operation(), legacy);
							TTCN_Logger.set_logmatch_buffer_len(previous_size);
						}
						if( !port__name.match(match_value.constGet_field_port__name(), legacy) ) {
							TTCN_Logger.log_logmatch_info(".port_name");
							port__name.log_match(match_value.constGet_field_port__name(), legacy);
							TTCN_Logger.set_logmatch_buffer_len(previous_size);
						}
						if( !compref.match(match_value.constGet_field_compref(), legacy) ) {
							TTCN_Logger.log_logmatch_info(".compref");
							compref.log_match(match_value.constGet_field_compref(), legacy);
							TTCN_Logger.set_logmatch_buffer_len(previous_size);
						}
						if( !msgid.match(match_value.constGet_field_msgid(), legacy) ) {
							TTCN_Logger.log_logmatch_info(".msgid");
							msgid.log_match(match_value.constGet_field_msgid(), legacy);
							TTCN_Logger.set_logmatch_buffer_len(previous_size);
						}
						if( !address__.match(match_value.constGet_field_address__(), legacy) ) {
							TTCN_Logger.log_logmatch_info(".address_");
							address__.log_match(match_value.constGet_field_address__(), legacy);
							TTCN_Logger.set_logmatch_buffer_len(previous_size);
						}
						if( !param__.match(match_value.constGet_field_param__(), legacy) ) {
							TTCN_Logger.log_logmatch_info(".param_");
							param__.log_match(match_value.constGet_field_param__(), legacy);
							TTCN_Logger.set_logmatch_buffer_len(previous_size);
						}
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
			if (template_selection == template_sel.SPECIFIC_VALUE) {
				TTCN_Logger.log_event_str("{ operation := ");
				operation.log_match(match_value.constGet_field_operation(), legacy);
				TTCN_Logger.log_event_str("{ port_name := ");
				port__name.log_match(match_value.constGet_field_port__name(), legacy);
				TTCN_Logger.log_event_str("{ compref := ");
				compref.log_match(match_value.constGet_field_compref(), legacy);
				TTCN_Logger.log_event_str("{ msgid := ");
				msgid.log_match(match_value.constGet_field_msgid(), legacy);
				TTCN_Logger.log_event_str("{ address_ := ");
				address__.log_match(match_value.constGet_field_address__(), legacy);
				TTCN_Logger.log_event_str("{ param_ := ");
				param__.log_match(match_value.constGet_field_param__(), legacy);
				TTCN_Logger.log_event_str(" }");
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
			encode_text_base(text_buf);
			switch (template_selection) {
			case OMIT_VALUE:
			case ANY_VALUE:
			case ANY_OR_OMIT:
				break;
			case SPECIFIC_VALUE:
				operation.encode_text(text_buf);
				port__name.encode_text(text_buf);
				compref.encode_text(text_buf);
				msgid.encode_text(text_buf);
				address__.encode_text(text_buf);
				param__.encode_text(text_buf);
				break;
			case VALUE_LIST:
			case COMPLEMENTED_LIST:
				text_buf.push_int(list_value.size());
				for (int i = 0; i < list_value.size(); i++) {
					list_value.get(i).encode_text(text_buf);
				}
				break;
			default:
				throw new TtcnError("Text encoder: Encoding an uninitialized/unsupported template of type @TitanLoggerApi.Port_Queue.");
			}
		}

		@Override
		public void decode_text(final Text_Buf text_buf) {
			clean_up();
			decode_text_base(text_buf);
			switch (template_selection) {
			case OMIT_VALUE:
			case ANY_VALUE:
			case ANY_OR_OMIT:
				break;
			case SPECIFIC_VALUE:
				operation = new Port__Queue_operation_template();
				operation.decode_text(text_buf);
				port__name = new TitanCharString_template();
				port__name.decode_text(text_buf);
				compref = new TitanInteger_template();
				compref.decode_text(text_buf);
				msgid = new TitanInteger_template();
				msgid.decode_text(text_buf);
				address__ = new TitanCharString_template();
				address__.decode_text(text_buf);
				param__ = new TitanCharString_template();
				param__.decode_text(text_buf);
				break;
			case VALUE_LIST:
			case COMPLEMENTED_LIST: {
				final int size = text_buf.pull_int().get_int();
				list_value = new ArrayList<Port__Queue_template>(size);
				for (int i = 0; i < size; i++) {
					final Port__Queue_template temp = new Port__Queue_template();
					temp.decode_text(text_buf);
					list_value.add(temp);
				}
				break;
			}
			default:
				throw new TtcnError("Text decoder: An unknown/unsupported selection was received in a template of type @TitanLoggerApi.Port_Queue.");
			}
		}

		@Override
		public void set_param(final Module_Parameter param) {
			param.basic_check(Module_Parameter.basic_check_bits_t.BC_TEMPLATE.getValue(), "record template");
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
			case MP_Value_List:
				if (param.get_size() > 6) {
					param.error(MessageFormat.format("record template of type @TitanLoggerApi.Port_Queue has 6 fields but list value has {0} fields.", param.get_size()));
				}
				if (param.get_size() > 0 && param.get_elem(0).get_type() != Module_Parameter.type_t.MP_NotUsed) {
					get_field_operation().set_param(param.get_elem(0));
				}
				if (param.get_size() > 1 && param.get_elem(1).get_type() != Module_Parameter.type_t.MP_NotUsed) {
					get_field_port__name().set_param(param.get_elem(1));
				}
				if (param.get_size() > 2 && param.get_elem(2).get_type() != Module_Parameter.type_t.MP_NotUsed) {
					get_field_compref().set_param(param.get_elem(2));
				}
				if (param.get_size() > 3 && param.get_elem(3).get_type() != Module_Parameter.type_t.MP_NotUsed) {
					get_field_msgid().set_param(param.get_elem(3));
				}
				if (param.get_size() > 4 && param.get_elem(4).get_type() != Module_Parameter.type_t.MP_NotUsed) {
					get_field_address__().set_param(param.get_elem(4));
				}
				if (param.get_size() > 5 && param.get_elem(5).get_type() != Module_Parameter.type_t.MP_NotUsed) {
					get_field_param__().set_param(param.get_elem(5));
				}
				break;
			case MP_Assignment_List: {
				final boolean value_used[] = new boolean[param.get_size()];
				for (int val_idx = 0; val_idx < param.get_size(); val_idx++) {
					final Module_Parameter curr_param = param.get_elem(val_idx);
					if ("operation".equals(curr_param.get_id().get_name())) {
						if (curr_param.get_type() != Module_Parameter.type_t.MP_NotUsed) {
							get_field_operation().set_param(curr_param);
						}
						value_used[val_idx] = true;
					}
				}
				for (int val_idx = 0; val_idx < param.get_size(); val_idx++) {
					final Module_Parameter curr_param = param.get_elem(val_idx);
					if ("port_name".equals(curr_param.get_id().get_name())) {
						if (curr_param.get_type() != Module_Parameter.type_t.MP_NotUsed) {
							get_field_port__name().set_param(curr_param);
						}
						value_used[val_idx] = true;
					}
				}
				for (int val_idx = 0; val_idx < param.get_size(); val_idx++) {
					final Module_Parameter curr_param = param.get_elem(val_idx);
					if ("compref".equals(curr_param.get_id().get_name())) {
						if (curr_param.get_type() != Module_Parameter.type_t.MP_NotUsed) {
							get_field_compref().set_param(curr_param);
						}
						value_used[val_idx] = true;
					}
				}
				for (int val_idx = 0; val_idx < param.get_size(); val_idx++) {
					final Module_Parameter curr_param = param.get_elem(val_idx);
					if ("msgid".equals(curr_param.get_id().get_name())) {
						if (curr_param.get_type() != Module_Parameter.type_t.MP_NotUsed) {
							get_field_msgid().set_param(curr_param);
						}
						value_used[val_idx] = true;
					}
				}
				for (int val_idx = 0; val_idx < param.get_size(); val_idx++) {
					final Module_Parameter curr_param = param.get_elem(val_idx);
					if ("address_".equals(curr_param.get_id().get_name())) {
						if (curr_param.get_type() != Module_Parameter.type_t.MP_NotUsed) {
							get_field_address__().set_param(curr_param);
						}
						value_used[val_idx] = true;
					}
				}
				for (int val_idx = 0; val_idx < param.get_size(); val_idx++) {
					final Module_Parameter curr_param = param.get_elem(val_idx);
					if ("param_".equals(curr_param.get_id().get_name())) {
						if (curr_param.get_type() != Module_Parameter.type_t.MP_NotUsed) {
							get_field_param__().set_param(curr_param);
						}
						value_used[val_idx] = true;
					}
				}
				for (int val_idx = 0; val_idx < param.get_size(); val_idx++) {
					if (!value_used[val_idx]) {
						final Module_Parameter curr_param = param.get_elem(val_idx);
						curr_param.error(MessageFormat.format("Non existent field name in type @TitanLoggerApi.Port_Queue: {0}", curr_param.get_id().get_name()));
						break;
					}
				}
				break;
			}
			default:
				param.type_error("record template", "@TitanLoggerApi.Port_Queue");
				break;
			}
			is_ifPresent = param.get_ifpresent();
		}

		@Override
		public void check_restriction(final template_res restriction, final String name, final boolean legacy) {
			if (template_selection == template_sel.UNINITIALIZED_TEMPLATE) {
				return;
			}
			switch ((name != null && restriction == template_res.TR_VALUE) ? template_res.TR_OMIT : restriction) {
			case TR_OMIT:
				if (template_selection == template_sel.OMIT_VALUE) {
					return;
				}
			case TR_VALUE:
				if (template_selection != template_sel.SPECIFIC_VALUE || is_ifPresent) {
					break;
				}
				this.operation.check_restriction(restriction, name == null ? "@TitanLoggerApi.Port_Queue" : name, legacy);
				this.port__name.check_restriction(restriction, name == null ? "@TitanLoggerApi.Port_Queue" : name, legacy);
				this.compref.check_restriction(restriction, name == null ? "@TitanLoggerApi.Port_Queue" : name, legacy);
				this.msgid.check_restriction(restriction, name == null ? "@TitanLoggerApi.Port_Queue" : name, legacy);
				this.address__.check_restriction(restriction, name == null ? "@TitanLoggerApi.Port_Queue" : name, legacy);
				this.param__.check_restriction(restriction, name == null ? "@TitanLoggerApi.Port_Queue" : name, legacy);
				return;
			case TR_PRESENT:
				if (!match_omit(legacy)) {
					return;
				}
				break;
			default:
				return;
			}
			throw new TtcnError(MessageFormat.format("Restriction `{0}'' on template of type {1} violated.", get_res_name(restriction), name == null ? "@TitanLoggerApi.Port_Queue" : name));
		}
	}