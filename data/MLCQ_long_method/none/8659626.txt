    public RecurrenceRule(GenericValue rule) throws RecurrenceRuleException {
        this.rule = rule;
        if (!"RecurrenceRule".equals(rule.getEntityName())) {
            throw new RecurrenceRuleException("Invalid RecurrenceRule Value object.");
        }
        init();
    }