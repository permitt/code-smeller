  private void initializePages() {
    initialCommandName = editedCommand.getName();

    pages.forEach(
        page -> {
          page.edit(editedCommand);
          page.setDirtyStateListener(
              () -> {
                updateDirtyState(isDirtyPage());
                view.setSaveEnabled(isDirtyPage());
              });
        });
  }