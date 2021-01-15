	public class XMLCMCellModifier implements ICellModifier, TreeExtension.ICellEditorProvider {
		public boolean canModify(Object element, String property) {
			boolean result = false;
			if (element instanceof Node) {
				Node node = (Node) element;
				if (property == VALUE_PROPERTY) {
					result = treeContentHelper.isEditable(node);
					if (result) {
						/* Set up the cell editor based on the element */
						CellEditor[] editors = getCellEditors();
						if (editors.length > 0) {
							if (editors[1] != null)
								editors[1].dispose();
							editors[1] = getCellEditor(element, 1);
							if (editors[1] instanceof TextCellEditor) {
								final CellListener listener = new CellListener(node, editors[1]);
								getColumnViewerEditor().addEditorActivationListener(listener);
								editors[1].addListener(listener);
							}
						}
					}
					
				}
			}
			return result;
		}

		public Object getValue(Object object, String property) {
			String result = null;
			if (object instanceof Node) {
				result = treeContentHelper.getNodeValue((Node) object);
			}
			return (result != null) ? result : ""; //$NON-NLS-1$
		}

		public void modify(Object element, String property, Object value) {
			Item item = (Item) element;
			String oldValue = treeContentHelper.getNodeValue((Node) item.getData());
			String newValue = value.toString();
			if ((newValue != null) && !newValue.equals(oldValue)) {
				treeContentHelper.setNodeValue((Node) item.getData(), value.toString(), getControl().getShell());
			}
		}

		public CellEditor getCellEditor(Object o, int col) {
			IPropertyDescriptor pd = propertyDescriptorFactory.createPropertyDescriptor(o);
			return pd != null ? pd.createPropertyEditor(XMLTableTreeViewer.this.getTree()) : null;
		}
	}