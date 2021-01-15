    public void testInvalidType_2() {
        Dialog dialog = getWarningDialog("Invalid",  "Is this invalid?");
        DialogCheck.assertDialog(dialog);
    }