public class SharingWizard {

	private static final SWTWorkbenchBot bot = new SWTWorkbenchBot();

	public ExistingOrNewPage openWizard(String ... projectNames) {
		SWTBotTree tree = bot.viewById(JavaUI.ID_PACKAGES).bot().tree();

		tree.select(projectNames);
		ContextMenuHelper.clickContextMenu(tree, "Team", "Share Project...");

		bot.table().getTableItem("Git").select();
		bot.button("Next >").click();

		return new ExistingOrNewPage();
	}
}