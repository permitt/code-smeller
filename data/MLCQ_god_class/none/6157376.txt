public class Application implements Serializable {

	/** serialVersionUID */
	private static final long serialVersionUID = 5675660442127228497L;

	private String name;

	private String url;

	/**
	 * @return name
	 */
	public String getName() {
		return name;
	}

	/**
	 * @param name
	 * @return this application
	 */
	public Application setName(String name) {
		this.name = name;
		return this;
	}

	/**
	 * @return url
	 */
	public String getUrl() {
		return url;
	}

	/**
	 * @param url
	 * @return this application
	 */
	public Application setUrl(String url) {
		this.url = url;
		return this;
	}
}