	@RequestMapping("/home")
	public String home(Model model) {
		model.addAttribute("name", "spring");
		return "home";
	}