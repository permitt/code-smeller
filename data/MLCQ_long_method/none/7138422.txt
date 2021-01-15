  public OptionsRequest(Map<String, String> headers,
                        List<HttpCookie> cookies,
                        Map<String, Object> queryParams,
                        Map<String, Class<?>> queryParamClasses,
                        ResourceSpec resourceSpec,
                        String baseUriTemplate,
                        Map<String, Object> pathKeys,
                        RestliRequestOptions requestOptions)
  {
    super(ResourceMethod.OPTIONS,
          null,
          headers,
          cookies,
          new OptionsResponseDecoder(),
          resourceSpec,
          queryParams,
          queryParamClasses,
          null,
          baseUriTemplate,
          pathKeys,
          requestOptions,
          null);
  }