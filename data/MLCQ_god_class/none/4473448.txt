	public static class RemoveNonUMLSEvents extends org.apache.uima.fit.component.JCasAnnotator_ImplBase {
		public static final String PARAM_GOLD_VIEW = "GoldView";

		@ConfigurationParameter(name = PARAM_GOLD_VIEW,mandatory=false)
		private String goldViewName = CAS.NAME_DEFAULT_SOFA;

		@Override
		public void process(JCas jCas) throws AnalysisEngineProcessException {
			JCas sysView;
			JCas goldView;
			try {
				sysView = jCas.getView(CAS.NAME_DEFAULT_SOFA);
				goldView = jCas.getView(PARAM_GOLD_VIEW);
			} catch (CASException e) {
				throw new AnalysisEngineProcessException(e);
			}
			for(TemporalTextRelation relation : Lists.newArrayList(JCasUtil.select(goldView, TemporalTextRelation.class))){
				Annotation arg1 = relation.getArg1().getArgument();
				Annotation arg2 = relation.getArg2().getArgument();
				boolean arg1Valid = false;
				boolean arg2Valid = false;
				for (EventMention event : JCasUtil.selectCovered(sysView, EventMention.class, arg1)){
					if(!event.getClass().equals(EventMention.class)){
						arg1Valid = true;
						break;
					}
				}
				for (EventMention event : JCasUtil.selectCovered(sysView, EventMention.class, arg2)){
					if(!event.getClass().equals(EventMention.class)){
						arg2Valid = true;
						break;
					}
				}
				if(arg1Valid && arg2Valid){
					// these are the kind we keep.
					continue;
				}
				arg1.removeFromIndexes();
				arg2.removeFromIndexes();
				relation.removeFromIndexes();
			}
		}   
	}