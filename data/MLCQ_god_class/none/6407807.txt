public class CopyDataToClipboardSerializer implements ISerializer {

    private final ILayerCell[][] copiedCells;
    private final CopyDataToClipboardCommand command;

    public CopyDataToClipboardSerializer(ILayerCell[][] copiedCells,
            CopyDataToClipboardCommand command) {
        this.copiedCells = copiedCells;
        this.command = command;
    }

    @Override
    public void serialize() {
        final String cellDelimeter = this.command.getCellDelimeter();
        final String rowDelimeter = this.command.getRowDelimeter();

        final TextTransfer textTransfer = TextTransfer.getInstance();
        final StringBuilder textData = new StringBuilder();
        int currentRow = 0;
        for (ILayerCell[] cells : this.copiedCells) {
            int currentCell = 0;
            for (ILayerCell cell : cells) {
                final String delimeter = ++currentCell < cells.length ? cellDelimeter
                        : ""; //$NON-NLS-1$
                if (cell != null) {
                    textData.append(getTextForCell(cell) + delimeter);
                } else {
                    textData.append(delimeter);
                }
            }
            if (++currentRow < this.copiedCells.length) {
                textData.append(rowDelimeter);
            }
        }
        if (textData.length() > 0) {
            final Clipboard clipboard = new Clipboard(Display.getDefault());
            try {
                clipboard.setContents(new Object[] { textData.toString() },
                        new Transfer[] { textTransfer });
            } finally {
                clipboard.dispose();
            }
        }
    }

    protected String getTextForCell(ILayerCell cell) {
        return String.valueOf(cell.getDataValue());
    }

    final protected CopyDataToClipboardCommand getCommand() {
        return this.command;
    }
}