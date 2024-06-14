# coding: utf-8

"""
    Finazon API

    ## API reference  Finazon is a comprehensive financial data marketplace that enables developers to effortlessly integrate a wide variety of global datasets, including stocks, ETFs, cryptocurrencies, and more, all with fully customizable parameters.  The Finazon API is built around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) principles, featuring resource-oriented URLs with predictable behavior. The API accepts [form-encoded](https://en.wikipedia.org/wiki/POST_(HTTP)#Use_for_submitting_web_forms) request bodies, returns JSON-encoded responses, and utilizes standard HTTP response codes, authentication methods, and verbs.  The Finazon API doesn't support bulk updates. You can work on only one instrument per request.  ## Authentification  To authenticate requests, the Finazon API requires [API keys](https://finazon.io/account/developers/api-keys). You can obtain, view, and manage your API keys through the [Finazon Dashboard](https://finazon.io/account/home).  Your API keys hold significant privileges, so ensure their security by not sharing your secret API keys in publicly accessible areas, such as GitHub repositories, client-side code, or any other public platforms.  All API requests must be made over [HTTPS](http://en.wikipedia.org/wiki/HTTP_Secure). Calls over plain HTTP will fail, as will API requests without authentication.  Once you have your API key, include it in the parameters as follows:  ```bash https://api.finazon.io/latest?apikey=YOUR_API_KEY ```  Alternatively, pass it as a request header:  ```bash Authorization: apikey YOUR_API_KEY ```  ## Versioning  Whenever [backwards-incompatible](https://support.finazon.io/en/articles/7792859-api-upgrades#h_1e014217bf) changes are introduced to the API, a new dated version is released. Consult our [API upgrades guide](https://support.finazon.io/en/articles/7792859-api-upgrades) for more information on backwards compatibility, and view our API changelog for all API updates.  To always use the most up-to-date version, specify it as `/latest`:  ```bash https://api.finazon.io/latest ```  To access the most recent version of `v1.*`, use the following:  ```bash https://api.finazon.io/v1  ```  Or, to retrieve a specific version, call:  ```bash  https://api.finazon.io/v1.0 ```  Finazon will provide advance notice before deprecating older API versions, giving developers ample time to migrate to the updated version.  ## Endpoints structure  The Finazon API adheres to a consistent and structured pattern for its endpoints. The base URL for all requests is:  ```bash https://api.finazon.io/ ```  API endpoints are organized by resource types, including universal resources accessible across all publishers and publisher-specific resources. For example, the `/time_series` endpoint is compatible with all publishers that support this data format. Such responses will be standardized across all datasets, facilitating rapid integration of new markets into your applications.  ```bash https://api.finazon.io/latest/{{resource}} https://api.finazon.io/latest/time_series ```  Additionally, datasets may contain unique data exclusive to that dataset. In such cases, you might want to call a separate endpoint specifying the publisher to gather more data. For instance, the [Binance](https://finazon.io/dataset/binance) dataset time series can be requested as:  ```bash  https://api.finazon.io/latest/{{publisher}}/{{resource}} https://api.finazon.io/latest/binance/time_series ```  ## Parameters  Each API request has its own set of required and optional parameters. Parameters should be separated by an ampersand. Parameter names are case-sensitive, while parameter values are not. Each API request has its own set of required and optional parameters. Parameters should be separated by an ampersand. Parameter names and parameter values are case-sensitive  ```bash https://api.finazon.io/latest/time_series?dataset=sip_non_pro&ticker=AAPL&interval=1m&apikey= ```  ### Pagination  All API resources supporting bulk fetches are retrieved via \"list\" API methods. For example, you can list time series, list trades, and list quotes. These list API methods share a common structure, accepting at least these five parameters: `page`, `page_size`, `order`, `start_at`, and `end_at`.  The response of a list API method represents a single page in a reverse chronological stream of objects. If you do not specify `start_at` or `end_at`, you will receive the first page of this list, containing the newest objects. By default, you will receive 10 objects if you do not specify an alternative value for `page_size`. You can specify `start_at` equal to the T (timestamp) value of an item to retrieve the page of older objects occurring immediately after the specified timestamp in the reverse chronological stream. Similarly, you can specify `end_at` to receive a page of newer objects occurring immediately before the named object in the stream. You can use one of `start_at` or `end_at` or both. Objects in a page always appear in reverse chronological order, unless `order` is specified.  ## Errors  Finazon employs standard HTTP response codes to signify the success or failure of an API request. Generally, the response codes can be interpreted as follows:  `2xx` range codes indicate a successful request.  `4xx` range codes signify an error resulting from the provided information (e.g., invalid API key, API rate limit exceeded, etc.).  `5xx` range codes represent errors originating from Finazon's servers (these are rare occurrences).  For all `4xx`errors that can be addressed programmatically (e.g., endpoint not found), an error message is included to succinctly explain the reported issue. This allows developers to quickly identify and resolve errors in their API requests.   status | code | message | --------|:-----|:--------|  400 |  INVALID_PARAMETER | The **{parameter_name}** parameter is missing or invalid. |  400 |  INVALID_DATE_RANGE | The requested date range is invalid or unsupported. |  400 |  UNSUPPORTED_MARKET | The requested market or exchange is not supported by the API. Please check the supported markets and try again. |  400 |  INVALID_TICKER | The provided ticker is invalid or unsupported. |  401 |  UNAUTHORIZED_ACCESS | You are not authorized to access the requested endpoint or you have insufficient permissions. |  404 |  ENDPOINT_NOT_FOUND | The requested endpoint **{endpoint_name}** does not exist or could not be found. |  429 |  API_RATE_LIMIT_EXCEEDED | You have exceeded the allowed number of API calls within the minute. Please wait and try again later. |  401 |  INVALID_API_KEY | The provided API key is invalid or has expired. Please check your API key and try again |  408 |  REQUEST_TIMEOUT | The request took too long to complete and timed out. Please try again later or reduce the complexity of your query. |  503 |  DATA_UNAVAILABLE | The requested data is temporarily unavailable or not supported. Please try again later or check the availability of the data. |  500 |  INTERNAL_SERVER_ERROR | An error occurred on the server-side while processing the request. Please try again later. If the issue persists, contact support. |  # noqa: E501

    OpenAPI spec version: v1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ReferenceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_api_usage(self, **kwargs):  # noqa: E501
        """Api usage  # noqa: E501

        Returns a list of datasets with available API calls and limits.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_usage(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product: Product code
        :return: ApiUsageResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_api_usage_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_api_usage_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_api_usage_with_http_info(self, **kwargs):  # noqa: E501
        """Api usage  # noqa: E501

        Returns a list of datasets with available API calls and limits.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_usage_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product: Product code
        :return: ApiUsageResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_api_usage" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product' in params:
            query_params.append(('product', params['product']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api_usage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiUsageResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_datasets(self, **kwargs):  # noqa: E501
        """List of Finazon datasets  # noqa: E501

        Returns a list of all datasets available at Finazon.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_datasets(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Filter by Finazon's dataset code
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :return: DatasetsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_datasets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_datasets_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_datasets_with_http_info(self, **kwargs):  # noqa: E501
        """List of Finazon datasets  # noqa: E501

        Returns a list of all datasets available at Finazon.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_datasets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Filter by Finazon's dataset code
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :return: DatasetsResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datasets" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'code' in params:
            query_params.append(('code', params['code']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/datasets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DatasetsResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_exchanges_crypto(self, **kwargs):  # noqa: E501
        """List of crypto markets  # noqa: E501

        Returns a list of supported crypto markets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_exchanges_crypto(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :return: ExchangesCryptoResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_exchanges_crypto_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_exchanges_crypto_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_exchanges_crypto_with_http_info(self, **kwargs):  # noqa: E501
        """List of crypto markets  # noqa: E501

        Returns a list of supported crypto markets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_exchanges_crypto_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :return: ExchangesCryptoResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_exchanges_crypto" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/markets/crypto', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExchangesCryptoResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_exchanges_stocks(self, **kwargs):  # noqa: E501
        """List of stock markets  # noqa: E501

        Returns a list of supported stock markets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_exchanges_stocks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country: Filter by ISO 3166 alpha-2 code
        :param str name: Filter by market name
        :param str code: Filter by market identifier code (MIC) under ISO 10383 standard
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :return: ExchangesStocksResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_exchanges_stocks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_exchanges_stocks_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_exchanges_stocks_with_http_info(self, **kwargs):  # noqa: E501
        """List of stock markets  # noqa: E501

        Returns a list of supported stock markets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_exchanges_stocks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country: Filter by ISO 3166 alpha-2 code
        :param str name: Filter by market name
        :param str code: Filter by market identifier code (MIC) under ISO 10383 standard
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :return: ExchangesStocksResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country', 'name', 'code', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_exchanges_stocks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'code' in params:
            query_params.append(('code', params['code']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/markets/stocks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExchangesStocksResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_market_center(self, **kwargs):  # noqa: E501
        """List of market centers  # noqa: E501

        Returns a list of market centers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_market_center(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MarketCenterResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_market_center_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_market_center_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_market_center_with_http_info(self, **kwargs):  # noqa: E501
        """List of market centers  # noqa: E501

        Returns a list of market centers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_market_center_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MarketCenterResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_market_center" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/sip/market_center', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MarketCenterResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_publishers(self, **kwargs):  # noqa: E501
        """List of Finazon publishers  # noqa: E501

        Returns a list of all publishers available at Finazon.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_publishers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Filter by Finazon's publisher code
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :return: PublishersResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_publishers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_publishers_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_publishers_with_http_info(self, **kwargs):  # noqa: E501
        """List of Finazon publishers  # noqa: E501

        Returns a list of all publishers available at Finazon.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_publishers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Filter by Finazon's publisher code
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :return: PublishersResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_publishers" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'code' in params:
            query_params.append(('code', params['code']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/publishers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PublishersResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_symbols_crypto(self, **kwargs):  # noqa: E501
        """List of crypto pairs  # noqa: E501

        Returns a list of cryptocurrency ticker symbols (pairs). This list is updated daily.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_symbols_crypto(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code
        :param str ticker: Filter by ticker symbol
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :return: SymbolsCryptoResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_symbols_crypto_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_symbols_crypto_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_symbols_crypto_with_http_info(self, **kwargs):  # noqa: E501
        """List of crypto pairs  # noqa: E501

        Returns a list of cryptocurrency ticker symbols (pairs). This list is updated daily.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_symbols_crypto_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code
        :param str ticker: Filter by ticker symbol
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :return: SymbolsCryptoResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset', 'ticker', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_symbols_crypto" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dataset' in params:
            query_params.append(('dataset', params['dataset']))  # noqa: E501
        if 'ticker' in params:
            query_params.append(('ticker', params['ticker']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/tickers/crypto', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SymbolsCryptoResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_symbols_forex(self, **kwargs):  # noqa: E501
        """List of forex ticker symbols  # noqa: E501

        Returns a list of forex ticker symbols (pairs). This list is updated daily.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_symbols_forex(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ticker: Filter by ticker symbol
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :return: SymbolsForexResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_symbols_forex_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_symbols_forex_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_symbols_forex_with_http_info(self, **kwargs):  # noqa: E501
        """List of forex ticker symbols  # noqa: E501

        Returns a list of forex ticker symbols (pairs). This list is updated daily.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_symbols_forex_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ticker: Filter by ticker symbol
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :return: SymbolsForexResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ticker', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_symbols_forex" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ticker' in params:
            query_params.append(('ticker', params['ticker']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/tickers/forex', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SymbolsForexResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_symbols_stocks(self, **kwargs):  # noqa: E501
        """List of stock ticker symbols  # noqa: E501

        Returns a list of stock ticker symbols. This list is updated daily.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_symbols_stocks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str dataset: Filter by Finazon's dataset code
        :param str ticker: Filter by ticker symbol
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :return: SymbolsStocksResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_symbols_stocks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_symbols_stocks_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_symbols_stocks_with_http_info(self, **kwargs):  # noqa: E501
        """List of stock ticker symbols  # noqa: E501

        Returns a list of stock ticker symbols. This list is updated daily.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_symbols_stocks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str dataset: Filter by Finazon's dataset code
        :param str ticker: Filter by ticker symbol
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :return: SymbolsStocksResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cqs', 'cik', 'cusip', 'isin', 'composite_figi', 'share_figi', 'lei', 'dataset', 'ticker', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_symbols_stocks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cqs' in params:
            query_params.append(('cqs', params['cqs']))  # noqa: E501
        if 'cik' in params:
            query_params.append(('cik', params['cik']))  # noqa: E501
        if 'cusip' in params:
            query_params.append(('cusip', params['cusip']))  # noqa: E501
        if 'isin' in params:
            query_params.append(('isin', params['isin']))  # noqa: E501
        if 'composite_figi' in params:
            query_params.append(('composite_figi', params['composite_figi']))  # noqa: E501
        if 'share_figi' in params:
            query_params.append(('share_figi', params['share_figi']))  # noqa: E501
        if 'lei' in params:
            query_params.append(('lei', params['lei']))  # noqa: E501
        if 'dataset' in params:
            query_params.append(('dataset', params['dataset']))  # noqa: E501
        if 'ticker' in params:
            query_params.append(('ticker', params['ticker']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/tickers/stocks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SymbolsStocksResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_symbols_us_stocks(self, **kwargs):  # noqa: E501
        """List of US stock ticker symbols  # noqa: E501

        Returns a list of US stock ticker symbols. This list is updated daily.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_symbols_us_stocks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str ticker: Filter by ticker symbol
        :return: SymbolsUSStocksResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_symbols_us_stocks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_symbols_us_stocks_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_symbols_us_stocks_with_http_info(self, **kwargs):  # noqa: E501
        """List of US stock ticker symbols  # noqa: E501

        Returns a list of US stock ticker symbols. This list is updated daily.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_symbols_us_stocks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str ticker: Filter by ticker symbol
        :return: SymbolsUSStocksResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cqs', 'cik', 'cusip', 'isin', 'composite_figi', 'share_figi', 'lei', 'page', 'page_size', 'ticker']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_symbols_us_stocks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cqs' in params:
            query_params.append(('cqs', params['cqs']))  # noqa: E501
        if 'cik' in params:
            query_params.append(('cik', params['cik']))  # noqa: E501
        if 'cusip' in params:
            query_params.append(('cusip', params['cusip']))  # noqa: E501
        if 'isin' in params:
            query_params.append(('isin', params['isin']))  # noqa: E501
        if 'composite_figi' in params:
            query_params.append(('composite_figi', params['composite_figi']))  # noqa: E501
        if 'share_figi' in params:
            query_params.append(('share_figi', params['share_figi']))  # noqa: E501
        if 'lei' in params:
            query_params.append(('lei', params['lei']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'ticker' in params:
            query_params.append(('ticker', params['ticker']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/tickers/us_stocks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SymbolsUSStocksResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
