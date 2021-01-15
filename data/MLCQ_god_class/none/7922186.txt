public class JbpmSequenceFlowPropertySection extends SequenceFlowPropertySection {

	@Override
	public boolean appliesTo(IWorkbenchPart part, ISelection selection) {
		if (super.appliesTo(part, selection)) {
			EObject be = getBusinessObjectForSelection(selection);
			if (be instanceof SequenceFlow) {
				// only show this tab if the sequence flow is attached to a Gateway
				if (((SequenceFlow) be).getSourceRef() instanceof Gateway) {
					Gateway gateway = (Gateway) ((SequenceFlow) be).getSourceRef();
					// hide this tab if the "condition expression" on the Sequence Flow
					// or the (possibly) attached Gateway's "default flow" feature is disabled
					boolean conditionEnabled = isModelObjectEnabled(
							Bpmn2Package.eINSTANCE.getSequenceFlow(),
							Bpmn2Package.eINSTANCE.getSequenceFlow_ConditionExpression());

					boolean defaultEnabled = true;
					EStructuralFeature defaultFeature = gateway.eClass().getEStructuralFeature("default"); //$NON-NLS-1$
					if (defaultFeature!=null) {
						if (!isModelObjectEnabled(gateway.eClass(), defaultFeature))
							defaultEnabled = false;
					}
					return conditionEnabled || defaultEnabled;
				}
			}
		}
		return false;
	}

	@Override
	protected AbstractDetailComposite createSectionRoot() {
		return new JbpmSequenceFlowDetailComposite(this);
	}

	@Override
	public AbstractDetailComposite createSectionRoot(Composite parent, int style) {
		return new JbpmSequenceFlowDetailComposite(parent,style);
	}
}