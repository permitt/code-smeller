	@Override
	public ListCompositeContentProvider getContentProvider(EObject object, EStructuralFeature feature, EList<EObject>list) {
		if (contentProvider==null) {
			contentProvider = new ListCompositeContentProvider(this, object, feature, list) {
				@Override
				public Object[] getElements(Object inputElement) {
					
					Object elements[] = super.getElements(inputElement);
					List<Property> props = null;
					ModelExtensionDescriptor med = null;
					ExtendedPropertiesAdapter<?> adapter = ExtendedPropertiesAdapter.adapt(activity);
					if (adapter!=null) {
						// look for it in the property adapter first
						med = adapter.getProperty(ModelExtensionDescriptor.class);
					}

					if (med==null) {
						// not found? get the Custom Task ID from the Task object
						String id = CustomElementFeatureContainer.findId(activity);
						if (id!=null) {
							// and look it up in the Target Runtime's list of
							// Custom Task Descriptors
					    	TargetRuntime rt = TargetRuntime.getRuntime(activity);
					    	med = rt.getCustomTask(id);
						}
					}
					if (med!=null) {
						if (JbpmIoParametersListComposite.this.isInput)
							props = med.getProperties("ioSpecification/dataInputs/name"); //$NON-NLS-1$
						else
							props = med.getProperties("ioSpecification/dataOutputs/name"); //$NON-NLS-1$
					}
					
					List<Object> filtered = new ArrayList<Object>();
					for (Object e : elements) {
						boolean skip = false;
						EStructuralFeature f = ((EObject)e).eClass().getEStructuralFeature("name"); //$NON-NLS-1$
						if (f!=null) {
							Object elementName = (String) ((EObject)e).eGet(f);
							if (props!=null) {
								for (Property p : props) {
									Object propName = p.getFirstStringValue();
									if (elementName!=null && propName!=null && elementName.equals(propName)) {
										skip = true;
										break;
									}
								}
							}
							if (activity instanceof SendTask) {
								if ("Message".equals(elementName)) {
									skip = true;
								}
							}
							else if (activity instanceof ReceiveTask) {
								if ("Message".equals(elementName)) {
									skip = true;
								}
//								else if ("MessageId".equals(elementName)) {
//									skip = true;
//								}
							}
							else if (activity instanceof ServiceTask) {
								if ("Parameter".equals(elementName)) {
									skip = true;
								}
								else if ("Result".equals(elementName)) {
									skip = true;
								}
								// TODO: these should be automatically added by the "Service Task" tab...
//								else if ("Interface".equals(elementName)) {
//									skip = true;
//								}
//								else if ("Operation".equals(elementName)) {
//									skip = true;
//								}
//								else if ("ParameterType".equals(elementName)) {
//									skip = true;
//								}
							}
						}
						if (!skip)
							filtered.add(e);
					}
					return filtered.toArray();
				}
			};
		}
		return contentProvider;
	}