    static class CreateSerializer extends JsonSerializer<ScopeAndMetricOnlySchemaRecordList> {

        @Override
        public void serialize(ScopeAndMetricOnlySchemaRecordList list, JsonGenerator jgen, SerializerProvider provider)
                throws IOException {

            ObjectMapper mapper = new ObjectMapper();
            mapper.setSerializationInclusion(Include.NON_NULL);

            for(Map.Entry<String, ScopeAndMetricOnlySchemaRecord> entry : list._idToSchemaRecordMap.entrySet()) {
                String fieldsData = mapper.writeValueAsString(entry.getValue());
                SchemaRecordList.addCreateJson(jgen, entry.getKey(), fieldsData);
            }
        }
    }