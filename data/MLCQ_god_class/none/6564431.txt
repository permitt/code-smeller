public class WebClientProvider implements ClientProvider {

  @Override
  public boolean accept( HttpServletRequest request ) {
    return true;
  }

  @Override
  public Client getClient() {
    return new WebClient();
  }

}