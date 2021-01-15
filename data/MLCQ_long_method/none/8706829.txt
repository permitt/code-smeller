	public static final boolean gdk_event_get_scroll_direction(long /*int*/ event, int [] direction) {
		lock.lock();
		try {
			return _gdk_event_get_scroll_direction(event, direction);
		} finally {
			lock.unlock();
		}
	}