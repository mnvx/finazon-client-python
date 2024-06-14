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


class TechnicalIndicatorApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_technical_indicator_atr(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """ATR Technical indicators  # noqa: E501

        The Average True Range (ATR) is a volatility indicator that measures the average range of price movement over a specified period, helping traders assess market volatility.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_atr(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param int time_period: Number of periods to average over.
        :return: list[TechnicalIndicatorResponseAtr]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_technical_indicator_atr_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
        else:
            (data) = self.get_technical_indicator_atr_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
            return data

    def get_technical_indicator_atr_with_http_info(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """ATR Technical indicators  # noqa: E501

        The Average True Range (ATR) is a volatility indicator that measures the average range of price movement over a specified period, helping traders assess market volatility.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_atr_with_http_info(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param int time_period: Number of periods to average over.
        :return: list[TechnicalIndicatorResponseAtr]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset', 'ticker', 'interval', 'cqs', 'cik', 'cusip', 'isin', 'composite_figi', 'share_figi', 'lei', 'market', 'country', 'start_at', 'end_at', 'page', 'page_size', 'order', 'prepost', 'adjust', 'time_period']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_technical_indicator_atr" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_technical_indicator_atr`")  # noqa: E501
        # verify the required parameter 'ticker' is set
        if ('ticker' not in params or
                params['ticker'] is None):
            raise ValueError("Missing the required parameter `ticker` when calling `get_technical_indicator_atr`")  # noqa: E501
        # verify the required parameter 'interval' is set
        if ('interval' not in params or
                params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `get_technical_indicator_atr`")  # noqa: E501

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
        if 'interval' in params:
            query_params.append(('interval', params['interval']))  # noqa: E501
        if 'market' in params:
            query_params.append(('market', params['market']))  # noqa: E501
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
        if 'start_at' in params:
            query_params.append(('start_at', params['start_at']))  # noqa: E501
        if 'end_at' in params:
            query_params.append(('end_at', params['end_at']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'prepost' in params:
            query_params.append(('prepost', params['prepost']))  # noqa: E501
        if 'adjust' in params:
            query_params.append(('adjust', params['adjust']))  # noqa: E501
        if 'time_period' in params:
            query_params.append(('time_period', params['time_period']))  # noqa: E501

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
            '/time_series/atr', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TechnicalIndicatorResponseAtr]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_technical_indicator_b_bands(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """Overlap Studies  # noqa: E501

        Bollinger Bands (BBANDS) are volatility bands placed above and below a moving average, measuring price volatility and helping traders identify potential overbought or oversold conditions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_b_bands(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param str series_type: Specifies the price data type on which technical indicator is calculated
        :param int time_period: Number of periods to average over.
        :param float sd: Number of standard deviations
        :param str ma_type: The type of moving average used, such as SMA or EMA
        :return: list[TechnicalIndicatorResponseBBands]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_technical_indicator_b_bands_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
        else:
            (data) = self.get_technical_indicator_b_bands_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
            return data

    def get_technical_indicator_b_bands_with_http_info(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """Overlap Studies  # noqa: E501

        Bollinger Bands (BBANDS) are volatility bands placed above and below a moving average, measuring price volatility and helping traders identify potential overbought or oversold conditions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_b_bands_with_http_info(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param str series_type: Specifies the price data type on which technical indicator is calculated
        :param int time_period: Number of periods to average over.
        :param float sd: Number of standard deviations
        :param str ma_type: The type of moving average used, such as SMA or EMA
        :return: list[TechnicalIndicatorResponseBBands]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset', 'ticker', 'interval', 'cqs', 'cik', 'cusip', 'isin', 'composite_figi', 'share_figi', 'lei', 'market', 'country', 'start_at', 'end_at', 'page', 'page_size', 'order', 'prepost', 'adjust', 'series_type', 'time_period', 'sd', 'ma_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_technical_indicator_b_bands" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_technical_indicator_b_bands`")  # noqa: E501
        # verify the required parameter 'ticker' is set
        if ('ticker' not in params or
                params['ticker'] is None):
            raise ValueError("Missing the required parameter `ticker` when calling `get_technical_indicator_b_bands`")  # noqa: E501
        # verify the required parameter 'interval' is set
        if ('interval' not in params or
                params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `get_technical_indicator_b_bands`")  # noqa: E501

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
        if 'interval' in params:
            query_params.append(('interval', params['interval']))  # noqa: E501
        if 'market' in params:
            query_params.append(('market', params['market']))  # noqa: E501
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
        if 'start_at' in params:
            query_params.append(('start_at', params['start_at']))  # noqa: E501
        if 'end_at' in params:
            query_params.append(('end_at', params['end_at']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'prepost' in params:
            query_params.append(('prepost', params['prepost']))  # noqa: E501
        if 'adjust' in params:
            query_params.append(('adjust', params['adjust']))  # noqa: E501
        if 'series_type' in params:
            query_params.append(('series_type', params['series_type']))  # noqa: E501
        if 'time_period' in params:
            query_params.append(('time_period', params['time_period']))  # noqa: E501
        if 'sd' in params:
            query_params.append(('sd', params['sd']))  # noqa: E501
        if 'ma_type' in params:
            query_params.append(('ma_type', params['ma_type']))  # noqa: E501

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
            '/time_series/bbands', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TechnicalIndicatorResponseBBands]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_technical_indicator_ichimoku(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """Overlap Studies  # noqa: E501

        The Ichimoku Cloud (ICHIMOKU) is a comprehensive trend-following indicator that combines multiple moving averages and support/resistance levels to help traders identify potential entry and exit points, trend direction, and momentum.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_ichimoku(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param int conversion_line_period: The time period used for generating the conversation line
        :param int base_line_period: The time period used for generating the base line
        :param int leading_span_b_period: The time period used for generating the leading span B line
        :param int lagging_span_period: The time period used for generating the lagging span line
        :param bool include_ahead_span_period: Indicates whether to include ahead span period
        :return: list[TechnicalIndicatorResponseIchimoku]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_technical_indicator_ichimoku_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
        else:
            (data) = self.get_technical_indicator_ichimoku_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
            return data

    def get_technical_indicator_ichimoku_with_http_info(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """Overlap Studies  # noqa: E501

        The Ichimoku Cloud (ICHIMOKU) is a comprehensive trend-following indicator that combines multiple moving averages and support/resistance levels to help traders identify potential entry and exit points, trend direction, and momentum.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_ichimoku_with_http_info(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param int conversion_line_period: The time period used for generating the conversation line
        :param int base_line_period: The time period used for generating the base line
        :param int leading_span_b_period: The time period used for generating the leading span B line
        :param int lagging_span_period: The time period used for generating the lagging span line
        :param bool include_ahead_span_period: Indicates whether to include ahead span period
        :return: list[TechnicalIndicatorResponseIchimoku]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset', 'ticker', 'interval', 'cqs', 'cik', 'cusip', 'isin', 'composite_figi', 'share_figi', 'lei', 'market', 'country', 'start_at', 'end_at', 'page', 'page_size', 'order', 'prepost', 'adjust', 'conversion_line_period', 'base_line_period', 'leading_span_b_period', 'lagging_span_period', 'include_ahead_span_period']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_technical_indicator_ichimoku" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_technical_indicator_ichimoku`")  # noqa: E501
        # verify the required parameter 'ticker' is set
        if ('ticker' not in params or
                params['ticker'] is None):
            raise ValueError("Missing the required parameter `ticker` when calling `get_technical_indicator_ichimoku`")  # noqa: E501
        # verify the required parameter 'interval' is set
        if ('interval' not in params or
                params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `get_technical_indicator_ichimoku`")  # noqa: E501

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
        if 'interval' in params:
            query_params.append(('interval', params['interval']))  # noqa: E501
        if 'market' in params:
            query_params.append(('market', params['market']))  # noqa: E501
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
        if 'start_at' in params:
            query_params.append(('start_at', params['start_at']))  # noqa: E501
        if 'end_at' in params:
            query_params.append(('end_at', params['end_at']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'prepost' in params:
            query_params.append(('prepost', params['prepost']))  # noqa: E501
        if 'adjust' in params:
            query_params.append(('adjust', params['adjust']))  # noqa: E501
        if 'conversion_line_period' in params:
            query_params.append(('conversion_line_period', params['conversion_line_period']))  # noqa: E501
        if 'base_line_period' in params:
            query_params.append(('base_line_period', params['base_line_period']))  # noqa: E501
        if 'leading_span_b_period' in params:
            query_params.append(('leading_span_b_period', params['leading_span_b_period']))  # noqa: E501
        if 'lagging_span_period' in params:
            query_params.append(('lagging_span_period', params['lagging_span_period']))  # noqa: E501
        if 'include_ahead_span_period' in params:
            query_params.append(('include_ahead_span_period', params['include_ahead_span_period']))  # noqa: E501

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
            '/time_series/ichimoku', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TechnicalIndicatorResponseIchimoku]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_technical_indicator_ma(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """Overlap Studies  # noqa: E501

        The Moving Average (MA) is a smoothing indicator that calculates the average price of a security over a specified period, helping traders identify trends and potential support or resistance levels.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_ma(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param str series_type: Specifies the price data type on which technical indicator is calculated
        :param int time_period: Number of periods to average over.
        :param str ma_type: The type of moving average used, such as SMA or EMA
        :return: list[TechnicalIndicatorResponseMa]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_technical_indicator_ma_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
        else:
            (data) = self.get_technical_indicator_ma_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
            return data

    def get_technical_indicator_ma_with_http_info(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """Overlap Studies  # noqa: E501

        The Moving Average (MA) is a smoothing indicator that calculates the average price of a security over a specified period, helping traders identify trends and potential support or resistance levels.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_ma_with_http_info(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param str series_type: Specifies the price data type on which technical indicator is calculated
        :param int time_period: Number of periods to average over.
        :param str ma_type: The type of moving average used, such as SMA or EMA
        :return: list[TechnicalIndicatorResponseMa]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset', 'ticker', 'interval', 'cqs', 'cik', 'cusip', 'isin', 'composite_figi', 'share_figi', 'lei', 'market', 'country', 'start_at', 'end_at', 'page', 'page_size', 'order', 'prepost', 'adjust', 'series_type', 'time_period', 'ma_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_technical_indicator_ma" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_technical_indicator_ma`")  # noqa: E501
        # verify the required parameter 'ticker' is set
        if ('ticker' not in params or
                params['ticker'] is None):
            raise ValueError("Missing the required parameter `ticker` when calling `get_technical_indicator_ma`")  # noqa: E501
        # verify the required parameter 'interval' is set
        if ('interval' not in params or
                params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `get_technical_indicator_ma`")  # noqa: E501

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
        if 'interval' in params:
            query_params.append(('interval', params['interval']))  # noqa: E501
        if 'market' in params:
            query_params.append(('market', params['market']))  # noqa: E501
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
        if 'start_at' in params:
            query_params.append(('start_at', params['start_at']))  # noqa: E501
        if 'end_at' in params:
            query_params.append(('end_at', params['end_at']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'prepost' in params:
            query_params.append(('prepost', params['prepost']))  # noqa: E501
        if 'adjust' in params:
            query_params.append(('adjust', params['adjust']))  # noqa: E501
        if 'series_type' in params:
            query_params.append(('series_type', params['series_type']))  # noqa: E501
        if 'time_period' in params:
            query_params.append(('time_period', params['time_period']))  # noqa: E501
        if 'ma_type' in params:
            query_params.append(('ma_type', params['ma_type']))  # noqa: E501

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
            '/time_series/ma', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TechnicalIndicatorResponseMa]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_technical_indicator_macd(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """Momentum Indicators  # noqa: E501

        The Moving Average Convergence Divergence (MACD) is a momentum indicator that measures the difference between two moving averages, with a signal line used to identify potential trend reversals and trading opportunities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_macd(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param str series_type: Specifies the price data type on which technical indicator is calculated
        :param int fast_period: Number of periods for fast moving average
        :param int slow_period: Number of periods for slow moving average
        :param int signal_period: The time period used for generating the signal line
        :return: list[TechnicalIndicatorResponseMacd]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_technical_indicator_macd_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
        else:
            (data) = self.get_technical_indicator_macd_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
            return data

    def get_technical_indicator_macd_with_http_info(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """Momentum Indicators  # noqa: E501

        The Moving Average Convergence Divergence (MACD) is a momentum indicator that measures the difference between two moving averages, with a signal line used to identify potential trend reversals and trading opportunities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_macd_with_http_info(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param str series_type: Specifies the price data type on which technical indicator is calculated
        :param int fast_period: Number of periods for fast moving average
        :param int slow_period: Number of periods for slow moving average
        :param int signal_period: The time period used for generating the signal line
        :return: list[TechnicalIndicatorResponseMacd]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset', 'ticker', 'interval', 'cqs', 'cik', 'cusip', 'isin', 'composite_figi', 'share_figi', 'lei', 'market', 'country', 'start_at', 'end_at', 'page', 'page_size', 'order', 'prepost', 'adjust', 'series_type', 'fast_period', 'slow_period', 'signal_period']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_technical_indicator_macd" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_technical_indicator_macd`")  # noqa: E501
        # verify the required parameter 'ticker' is set
        if ('ticker' not in params or
                params['ticker'] is None):
            raise ValueError("Missing the required parameter `ticker` when calling `get_technical_indicator_macd`")  # noqa: E501
        # verify the required parameter 'interval' is set
        if ('interval' not in params or
                params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `get_technical_indicator_macd`")  # noqa: E501

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
        if 'interval' in params:
            query_params.append(('interval', params['interval']))  # noqa: E501
        if 'market' in params:
            query_params.append(('market', params['market']))  # noqa: E501
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
        if 'start_at' in params:
            query_params.append(('start_at', params['start_at']))  # noqa: E501
        if 'end_at' in params:
            query_params.append(('end_at', params['end_at']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'prepost' in params:
            query_params.append(('prepost', params['prepost']))  # noqa: E501
        if 'adjust' in params:
            query_params.append(('adjust', params['adjust']))  # noqa: E501
        if 'series_type' in params:
            query_params.append(('series_type', params['series_type']))  # noqa: E501
        if 'fast_period' in params:
            query_params.append(('fast_period', params['fast_period']))  # noqa: E501
        if 'slow_period' in params:
            query_params.append(('slow_period', params['slow_period']))  # noqa: E501
        if 'signal_period' in params:
            query_params.append(('signal_period', params['signal_period']))  # noqa: E501

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
            '/time_series/macd', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TechnicalIndicatorResponseMacd]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_technical_indicator_obv(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """Volume Indicators  # noqa: E501

        The On Balance Volume (OBV) indicator is a cumulative volume-based tool used to measure buying and selling pressure, helping traders identify potential price trends and reversals.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_obv(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param str series_type: Specifies the price data type on which technical indicator is calculated
        :return: list[TechnicalIndicatorResponseObv]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_technical_indicator_obv_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
        else:
            (data) = self.get_technical_indicator_obv_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
            return data

    def get_technical_indicator_obv_with_http_info(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """Volume Indicators  # noqa: E501

        The On Balance Volume (OBV) indicator is a cumulative volume-based tool used to measure buying and selling pressure, helping traders identify potential price trends and reversals.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_obv_with_http_info(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param str series_type: Specifies the price data type on which technical indicator is calculated
        :return: list[TechnicalIndicatorResponseObv]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset', 'ticker', 'interval', 'cqs', 'cik', 'cusip', 'isin', 'composite_figi', 'share_figi', 'lei', 'market', 'country', 'start_at', 'end_at', 'page', 'page_size', 'order', 'prepost', 'adjust', 'series_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_technical_indicator_obv" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_technical_indicator_obv`")  # noqa: E501
        # verify the required parameter 'ticker' is set
        if ('ticker' not in params or
                params['ticker'] is None):
            raise ValueError("Missing the required parameter `ticker` when calling `get_technical_indicator_obv`")  # noqa: E501
        # verify the required parameter 'interval' is set
        if ('interval' not in params or
                params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `get_technical_indicator_obv`")  # noqa: E501

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
        if 'interval' in params:
            query_params.append(('interval', params['interval']))  # noqa: E501
        if 'market' in params:
            query_params.append(('market', params['market']))  # noqa: E501
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
        if 'start_at' in params:
            query_params.append(('start_at', params['start_at']))  # noqa: E501
        if 'end_at' in params:
            query_params.append(('end_at', params['end_at']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'prepost' in params:
            query_params.append(('prepost', params['prepost']))  # noqa: E501
        if 'adjust' in params:
            query_params.append(('adjust', params['adjust']))  # noqa: E501
        if 'series_type' in params:
            query_params.append(('series_type', params['series_type']))  # noqa: E501

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
            '/time_series/obv', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TechnicalIndicatorResponseObv]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_technical_indicator_rsi(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """Momentum Indicators  # noqa: E501

        The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements, helping traders identify potential overbought or oversold conditions and trend reversals.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_rsi(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param str series_type: Specifies the price data type on which technical indicator is calculated
        :param int time_period: Number of periods to average over
        :return: list[TechnicalIndicatorResponseRsi]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_technical_indicator_rsi_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
        else:
            (data) = self.get_technical_indicator_rsi_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
            return data

    def get_technical_indicator_rsi_with_http_info(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """Momentum Indicators  # noqa: E501

        The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements, helping traders identify potential overbought or oversold conditions and trend reversals.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_rsi_with_http_info(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param str series_type: Specifies the price data type on which technical indicator is calculated
        :param int time_period: Number of periods to average over
        :return: list[TechnicalIndicatorResponseRsi]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset', 'ticker', 'interval', 'cqs', 'cik', 'cusip', 'isin', 'composite_figi', 'share_figi', 'lei', 'market', 'country', 'start_at', 'end_at', 'page', 'page_size', 'order', 'prepost', 'adjust', 'series_type', 'time_period']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_technical_indicator_rsi" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_technical_indicator_rsi`")  # noqa: E501
        # verify the required parameter 'ticker' is set
        if ('ticker' not in params or
                params['ticker'] is None):
            raise ValueError("Missing the required parameter `ticker` when calling `get_technical_indicator_rsi`")  # noqa: E501
        # verify the required parameter 'interval' is set
        if ('interval' not in params or
                params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `get_technical_indicator_rsi`")  # noqa: E501

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
        if 'interval' in params:
            query_params.append(('interval', params['interval']))  # noqa: E501
        if 'market' in params:
            query_params.append(('market', params['market']))  # noqa: E501
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
        if 'start_at' in params:
            query_params.append(('start_at', params['start_at']))  # noqa: E501
        if 'end_at' in params:
            query_params.append(('end_at', params['end_at']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'prepost' in params:
            query_params.append(('prepost', params['prepost']))  # noqa: E501
        if 'adjust' in params:
            query_params.append(('adjust', params['adjust']))  # noqa: E501
        if 'series_type' in params:
            query_params.append(('series_type', params['series_type']))  # noqa: E501
        if 'time_period' in params:
            query_params.append(('time_period', params['time_period']))  # noqa: E501

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
            '/time_series/rsi', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TechnicalIndicatorResponseRsi]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_technical_indicator_sar(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """Overlap Studies  # noqa: E501

        The Parabolic SAR (SAR) is a trend-following indicator that calculates potential support and resistance levels based on a security's price and time, helping traders identify potential entry and exit points.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_sar(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param float acceleration: Initial acceleration factor
        :param float maximum: Maximum value for the acceleration factor
        :return: list[TechnicalIndicatorResponseSar]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_technical_indicator_sar_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
        else:
            (data) = self.get_technical_indicator_sar_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
            return data

    def get_technical_indicator_sar_with_http_info(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """Overlap Studies  # noqa: E501

        The Parabolic SAR (SAR) is a trend-following indicator that calculates potential support and resistance levels based on a security's price and time, helping traders identify potential entry and exit points.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_sar_with_http_info(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param float acceleration: Initial acceleration factor
        :param float maximum: Maximum value for the acceleration factor
        :return: list[TechnicalIndicatorResponseSar]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset', 'ticker', 'interval', 'cqs', 'cik', 'cusip', 'isin', 'composite_figi', 'share_figi', 'lei', 'market', 'country', 'start_at', 'end_at', 'page', 'page_size', 'order', 'prepost', 'adjust', 'acceleration', 'maximum']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_technical_indicator_sar" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_technical_indicator_sar`")  # noqa: E501
        # verify the required parameter 'ticker' is set
        if ('ticker' not in params or
                params['ticker'] is None):
            raise ValueError("Missing the required parameter `ticker` when calling `get_technical_indicator_sar`")  # noqa: E501
        # verify the required parameter 'interval' is set
        if ('interval' not in params or
                params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `get_technical_indicator_sar`")  # noqa: E501

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
        if 'interval' in params:
            query_params.append(('interval', params['interval']))  # noqa: E501
        if 'market' in params:
            query_params.append(('market', params['market']))  # noqa: E501
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
        if 'start_at' in params:
            query_params.append(('start_at', params['start_at']))  # noqa: E501
        if 'end_at' in params:
            query_params.append(('end_at', params['end_at']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'prepost' in params:
            query_params.append(('prepost', params['prepost']))  # noqa: E501
        if 'adjust' in params:
            query_params.append(('adjust', params['adjust']))  # noqa: E501
        if 'acceleration' in params:
            query_params.append(('acceleration', params['acceleration']))  # noqa: E501
        if 'maximum' in params:
            query_params.append(('maximum', params['maximum']))  # noqa: E501

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
            '/time_series/sar', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TechnicalIndicatorResponseSar]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_technical_indicator_stoch(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """Momentum Indicators  # noqa: E501

        The Stochastic Oscillator (STOCH) is a momentum indicator that compares a security's closing price to its price range over a specified period, helping traders identify potential overbought or oversold conditions and trend reversals.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_stoch(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param int fast_k_period: The time period for the fast %K line in the Stochastic Oscillator
        :param int slow_k_period: The time period for the slow %K line in the Stochastic Oscillator
        :param int slow_d_period: The time period for the slow %D line in the Stochastic Oscillator
        :param str slow_kma_type: The type of slow %K Moving Average used
        :param str slow_dma_type: The type of slow Displaced Moving Average used
        :return: list[TechnicalIndicatorResponseStoch]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_technical_indicator_stoch_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
        else:
            (data) = self.get_technical_indicator_stoch_with_http_info(dataset, ticker, interval, **kwargs)  # noqa: E501
            return data

    def get_technical_indicator_stoch_with_http_info(self, dataset, ticker, interval, **kwargs):  # noqa: E501
        """Momentum Indicators  # noqa: E501

        The Stochastic Oscillator (STOCH) is a momentum indicator that compares a security's closing price to its price range over a specified period, helping traders identify potential overbought or oversold conditions and trend reversals.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_technical_indicator_stoch_with_http_info(dataset, ticker, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dataset: Filter by Finazon's dataset code (required)
        :param str ticker: Filter by ticker symbol (required)
        :param str interval: Interval between two consecutive points in time series (required)
        :param str cqs: Filter by cqs symbol
        :param str cik: Filter by cik code
        :param str cusip: Filter by cusip code
        :param str isin: Filter by isin code
        :param str composite_figi: Filter by composite figi code
        :param str share_figi: Filter by share class figi code
        :param str lei: Filter by lei code
        :param str market: Filter by market
        :param str country: Filter by ISO 3166 alpha-2 code
        :param int start_at: Filter output by start time using a UNIX timestamp
        :param int end_at: Filter output by end time using a UNIX timestamp
        :param int page: Specific page of a paginated result to be displayed
        :param int page_size: Number of items displayed per page in a paginated result
        :param str order: Sorting order of the output series
        :param bool prepost: Indicates whether data should be included for extended hours of trading
        :param str adjust: Apply adjusting for data (all, splits, dividends, none)
        :param int fast_k_period: The time period for the fast %K line in the Stochastic Oscillator
        :param int slow_k_period: The time period for the slow %K line in the Stochastic Oscillator
        :param int slow_d_period: The time period for the slow %D line in the Stochastic Oscillator
        :param str slow_kma_type: The type of slow %K Moving Average used
        :param str slow_dma_type: The type of slow Displaced Moving Average used
        :return: list[TechnicalIndicatorResponseStoch]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset', 'ticker', 'interval', 'cqs', 'cik', 'cusip', 'isin', 'composite_figi', 'share_figi', 'lei', 'market', 'country', 'start_at', 'end_at', 'page', 'page_size', 'order', 'prepost', 'adjust', 'fast_k_period', 'slow_k_period', 'slow_d_period', 'slow_kma_type', 'slow_dma_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_technical_indicator_stoch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_technical_indicator_stoch`")  # noqa: E501
        # verify the required parameter 'ticker' is set
        if ('ticker' not in params or
                params['ticker'] is None):
            raise ValueError("Missing the required parameter `ticker` when calling `get_technical_indicator_stoch`")  # noqa: E501
        # verify the required parameter 'interval' is set
        if ('interval' not in params or
                params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `get_technical_indicator_stoch`")  # noqa: E501

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
        if 'interval' in params:
            query_params.append(('interval', params['interval']))  # noqa: E501
        if 'market' in params:
            query_params.append(('market', params['market']))  # noqa: E501
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
        if 'start_at' in params:
            query_params.append(('start_at', params['start_at']))  # noqa: E501
        if 'end_at' in params:
            query_params.append(('end_at', params['end_at']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'prepost' in params:
            query_params.append(('prepost', params['prepost']))  # noqa: E501
        if 'adjust' in params:
            query_params.append(('adjust', params['adjust']))  # noqa: E501
        if 'fast_k_period' in params:
            query_params.append(('fast_k_period', params['fast_k_period']))  # noqa: E501
        if 'slow_k_period' in params:
            query_params.append(('slow_k_period', params['slow_k_period']))  # noqa: E501
        if 'slow_d_period' in params:
            query_params.append(('slow_d_period', params['slow_d_period']))  # noqa: E501
        if 'slow_kma_type' in params:
            query_params.append(('slow_kma_type', params['slow_kma_type']))  # noqa: E501
        if 'slow_dma_type' in params:
            query_params.append(('slow_dma_type', params['slow_dma_type']))  # noqa: E501

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
            '/time_series/stoch', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TechnicalIndicatorResponseStoch]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
