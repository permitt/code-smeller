    @RequestMapping("/ping")
    @ResponseBody
    public String ping() {
        return "pong";
    }