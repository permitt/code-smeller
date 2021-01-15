		public PREGEN__RECORD__OF__OCTETSTRING replace(final int index, final int len, final PREGEN__RECORD__OF__OCTETSTRING_template repl) {
			if (!repl.is_value()) {
				throw new TtcnError("The fourth argument of function replace() is a template with non-specific value.");
			}
			return replace(index, len, repl.valueof());
		}