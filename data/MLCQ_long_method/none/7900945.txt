      private void printRemove(ParsedRuleKeyFile file, Value value) {
        diffPrinter.printRemove(
            String.format(
                "%s: %s", String.join("/", pathComponents), valueAsReadableString(file, value)));
      }