public static final long /*int*/ webkit_get_favicon_database () {
	assert WEBKIT1 : Webkit1AssertMsg;
	lock.lock();
	try {
		return _webkit_get_favicon_database ();
	} finally {
		lock.unlock();
	}
}