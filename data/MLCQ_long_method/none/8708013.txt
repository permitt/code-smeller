private String[] splitString(String text) {
    String[] lines = new String[1];
    int start = 0, pos;
    do {
        pos = text.indexOf('\n', start);
        if (pos == -1) {
        	lines[lines.length - 1] = text.substring(start);
        } else {
            boolean crlf = (pos > 0) && (text.charAt(pos - 1) == '\r');
            lines[lines.length - 1] = text.substring(start, pos - (crlf ? 1 : 0));
            start = pos + 1;
            String[] newLines = new String[lines.length+1];
            System.arraycopy(lines, 0, newLines, 0, lines.length);
       		lines = newLines;
        }
    } while (pos != -1);
    return lines;
}