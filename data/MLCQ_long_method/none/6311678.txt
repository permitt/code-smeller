    @Then("^I find (\\d+) devices?$")
    public void checkDeviceListLength(int cnt) {
        Assert.assertNotNull(stepData.get("DeviceList"));
        Assert.assertEquals(cnt, ((DeviceListResultImpl) stepData.get("DeviceList")).getSize());
    }