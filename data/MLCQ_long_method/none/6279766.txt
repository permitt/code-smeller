		@Override
		Body process() throws IOException {
			Response.Body body = new Response.Body();
			if (objects.size() > 0) {
				body.objects = new ArrayList<>();
				for (LfsObject o : objects) {
					addObjectInfo(body, o);
				}
			}
			return body;
		}