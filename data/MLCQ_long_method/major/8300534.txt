	private void toggleNature(IProject project) {
		try {
			IProjectDescription description = project.getDescription();
			String[] natures = description.getNatureIds();
			for (int i = 0; i < natures.length; ++i) {
				if (IAcceleoConstants.ACCELEO_NATURE_ID.equals(natures[i])) {
					// Remove the nature
					String[] newNatures = new String[natures.length - 1];
					System.arraycopy(natures, 0, newNatures, 0, i);
					System.arraycopy(natures, i + 1, newNatures, i, natures.length - i - 1);
					description.setNatureIds(newNatures);
					project.setDescription(description, null);
					List<IFile> files = new ArrayList<IFile>();
					members(files, project);
					for (Iterator<IFile> itFiles = files.iterator(); itFiles.hasNext();) {
						IFile file = itFiles.next();
						try {
							file.deleteMarkers(AcceleoMarkerUtils.PROBLEM_MARKER_ID, false,
									IResource.DEPTH_ZERO);
							file.deleteMarkers(AcceleoMarkerUtils.WARNING_MARKER_ID, false,
									IResource.DEPTH_ZERO);
							file.deleteMarkers(AcceleoMarkerUtils.INFO_MARKER_ID, false, IResource.DEPTH_ZERO);
						} catch (CoreException e) {
							AcceleoUIActivator.getDefault().getLog()
									.log(new Status(IStatus.ERROR, AcceleoUIActivator.PLUGIN_ID, e
											.getMessage(), e));
						}
					}
					return;
				}
			}
			// Add the nature
			String[] newNatures = new String[natures.length + 2];
			System.arraycopy(natures, 0, newNatures, 2, natures.length);

			newNatures[0] = "org.eclipse.pde.PluginNature"; //$NON-NLS-1$
			newNatures[1] = IAcceleoConstants.ACCELEO_NATURE_ID;
			description.setNatureIds(newNatures);
			project.setDescription(description, null);

			// Override the ".project" anyway
			AcceleoProject acceleoProject = AcceleowizardmodelFactory.eINSTANCE.createAcceleoProject();
			acceleoProject.setName(project.getName());
			acceleoProject.setJre("J2SE-1.5"); //$NON-NLS-1$
			AcceleoUIGenerator.getDefault().generateDotProject(acceleoProject, project);

			// Generate the build.acceleo
			AcceleoUIGenerator.getDefault().generateBuildAcceleo(acceleoProject, project);

			IFile buildProperties = project.getFile("build.properties"); //$NON-NLS-1$
			if (buildProperties.exists()) {
				Properties properties = new Properties();
				try {
					properties.load(buildProperties.getContents());
					properties.put("customBuildCallbacks", "build.acceleo"); //$NON-NLS-1$//$NON-NLS-2$
					properties.store(new FileOutputStream(buildProperties.getLocation().toFile()), ""); //$NON-NLS-1$
				} catch (IOException e) {
					AcceleoUIActivator.log(e, true);
				}
			} else {
				AcceleoUIGenerator.getDefault().generateBuildProperties(acceleoProject, project);
			}

			project.refreshLocal(IResource.DEPTH_INFINITE, new NullProgressMonitor());
		} catch (CoreException e) {
			AcceleoUIActivator.getDefault().getLog().log(
					new Status(IStatus.ERROR, AcceleoUIActivator.PLUGIN_ID, e.getMessage(), e));
		}
	}