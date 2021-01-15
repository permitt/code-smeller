	static void scroll(ScrolledComposite scomp, int xoffset, int yoffset) {
		Point origin = scomp.getOrigin();
		Point contentSize = scomp.getContent().getSize();
		int xorigin = origin.x + xoffset;
		int yorigin = origin.y + yoffset;
		xorigin = Math.max(xorigin, 0);
		xorigin = Math.min(xorigin, contentSize.x - 1);
		yorigin = Math.max(yorigin, 0);
		yorigin = Math.min(yorigin, contentSize.y - 1);
		scomp.setOrigin(xorigin, yorigin);
	}