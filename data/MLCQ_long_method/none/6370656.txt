	private JobTreeElement[] findJobsToRemove(JobTreeElement info) {

		if (info.isJobInfo()) {
			Job myJob = ((JobInfo) info).getJob();

			if (myJob != null) {

				Object prop = myJob
						.getProperty(ProgressManagerUtil.KEEPONE_PROPERTY);
				if (prop instanceof Boolean && ((Boolean) prop).booleanValue()) {
					ArrayList<JobTreeElement> found = null;
					JobTreeElement[] all;
					synchronized (keptjobinfos) {
						all = keptjobinfos
								.toArray(new JobTreeElement[keptjobinfos.size()]);
					}
					for (JobTreeElement jte : all) {
						if (jte != info && jte.isJobInfo()) {
							Job job = ((JobInfo) jte).getJob();
							if (job != null && job != myJob
									&& job.belongsTo(myJob)) {
								if (found == null) {
									found = new ArrayList<>();
								}
								found.add(jte);
							}
						}
					}
					if (found != null) {
						return found
								.toArray(new JobTreeElement[found.size()]);
					}
				}
			}
		}
		return null;
	}