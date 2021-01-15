    @Override
    JSONObject getSimulateJsonResult(JSONObject requestJson) {
        JSONObject result = new JSONObject();
        try {
            result.put(KEY_RESULT_IS_SUPPORT, true);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return result;
    }