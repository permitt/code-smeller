  public static boolean validateTypeSize(final Component parent, final JTextField size) {
    if (validateTypeSize(size)) {
      return true;
    } else {
      CMessageBox.showWarning(parent, "Please enter a valid type size.");
      return false;
    }
  }