	public boolean operator_equals(final TitanOctetString_Element otherValue) {
		must_bound("Unbound left operand of octetstring element comparison.");
		otherValue.must_bound("Unbound right operand of octetstring comparison.");

		return str_val.get_nibble(nibble_pos) == otherValue.str_val.get_nibble(otherValue.nibble_pos);
	}